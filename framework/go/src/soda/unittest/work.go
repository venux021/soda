package unittest

import (
    "bufio"
    "fmt"
    "encoding/json"
    "os"
    "reflect"
    "time"
)

// object real type -> function parse data from json serial
var dataParsers map[reflect.Type]reflect.Value

// object real type -> function serialize data to json serial
var dataSerializers map[reflect.Type]reflect.Value

func init() {
    // typeMapping[from] = to
}

type TestInput struct {
    Args []interface{}   `json:"args"`
    Expected interface{} `json:"expected"`
    Id int               `json:"id"`
}

type TestOutput struct {
    Id int              `json:"id"`
    Success bool        `json:"success"`
    Result interface{}  `json:"result"`
    Elapse float64      `json:"elapse"`
}

type TestWork struct {
    Function reflect.Value
    ArgumentTypes []reflect.Type
    ReturnType reflect.Type
    CompareSerial bool

    argumentParsers  []reflect.Value
    // function values
    resultSerializer reflect.Value
    resultParser     reflect.Value
    validator        reflect.Value
}

func CreateWork(fn interface{}) *TestWork {
    work := new(TestWork)
    work.initialize(fn)
    return work
}

func (work *TestWork) SetResultSerializer(fn interface{}) {
    work.resultSerializer = reflect.ValueOf(fn)
}

func (work *TestWork) SetResultParser(fn interface{}) {
    work.resultParser = reflect.ValueOf(fn)
}

func (work *TestWork) SetValidator(fn interface{}) {
    work.validator = reflect.ValueOf(fn)
}

func (work *TestWork) SetArgParser(index int, fn interface{}) {
    work.argumentParsers[index] = reflect.ValueOf(fn)
}

func convByType(untyped interface{}, rtype reflect.Type) reflect.Value {
    content, _ := json.Marshal(untyped)
    v := reflect.New(rtype)
    p := v.Interface()
    json.Unmarshal(content, p)
    return v.Elem()
}

func (work *TestWork) initialize (fn interface{}) *TestWork {
    work.Function = reflect.ValueOf(fn)
    funcType := work.Function.Type()

    numArgs := funcType.NumIn()
    work.ArgumentTypes = make([]reflect.Type, numArgs)
    for i := 0; i < numArgs; i++ {
        work.ArgumentTypes[i] = funcType.In(i)
    }

    work.argumentParsers = make([]reflect.Value, numArgs)
    work.ReturnType = funcType.Out(0)
    valid := func(x, y interface{}) bool {
        return reflect.DeepEqual(x, y)
    }
    work.validator = reflect.ValueOf(valid)
    return work
}

func vals(values ...reflect.Value) []reflect.Value {
    return values
}

func compareByJsonSerial(a interface{}, b interface{}) bool {
    dataA, _ := json.Marshal(a)
    dataB, _ := json.Marshal(b)
    return reflect.DeepEqual(dataA, dataB)
}

func fromSerial(ser interface{}, workType reflect.Type, parser reflect.Value) reflect.Value {
    if !parser.IsValid() {
        parser = dataParsers[workType]
    }

    if parser.IsValid() {
        fromType := parser.Type().In(0)
        fromValue := convByType(ser, fromType)
        return parser.Call(vals(fromValue))[0]
    } else {
        return convByType(ser, workType)
    }
}

func toSerial(obj reflect.Value, serializer reflect.Value) reflect.Value {
    if !serializer.IsValid() {
        serializer = dataSerializers[obj.Type()]
    }

    if serializer.IsValid() {
        return serializer.Call(vals(obj))[0]
    } else {
        return obj
    }
}

func (work *TestWork) Run() {
    input := readStdin()
    testInput := TestInput {}
    if err := json.Unmarshal([]byte(input), &testInput); err != nil {
        fmt.Fprintf(os.Stderr, "JSON unmarshaling failed: %s", err)
        return
    }

    args := make([]reflect.Value, len(work.ArgumentTypes))
    for i := 0; i < len(testInput.Args); i++ {
        args[i] = fromSerial(testInput.Args[i], work.ArgumentTypes[i], work.argumentParsers[i])
    }

    startTime := time.Now()
    resultValue := work.Function.Call(args)[0]
    duration := time.Since(startTime)
    elapseMillis := float64(duration.Microseconds()) / 1000.0

    serialValue := toSerial(resultValue, work.resultSerializer)

    out := TestOutput {}
    out.Id = testInput.Id
    out.Result = serialValue.Interface()
    out.Elapse = elapseMillis

    success := true
    if testInput.Expected != nil {
        if !work.CompareSerial {
            expectValue := fromSerial(testInput.Expected, work.ReturnType, work.resultParser)
            success = work.validator.Call(vals(expectValue, resultValue))[0].Bool()
        } else {
            success = compareByJsonSerial(testInput.Expected, serialValue.Interface())
        }
    }

    out.Success = success

    jstring, err := json.Marshal(out)
    if err != nil {
        fmt.Fprintf(os.Stderr, "JSON marshaling failed: %s", err)
        return
    }
    fmt.Print(string(jstring))
}

func readStdin() string {
    scanner := bufio.NewScanner(os.Stdin)
    content := ""
    for scanner.Scan() {
        line := scanner.Text()
        content += line
    }
    return content
}

