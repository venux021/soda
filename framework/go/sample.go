package main

import (
    "fmt"
    "os"
    "encoding/json"
    "reflect"
    "soda/unittest"
)

func buildString(strs []string, times []int) string {
    res := ""
    for i := 0; i < len(strs); i++ {
        for j := 0; j < times[i]; j++ {
            res += strs[i]
        }
    }
    return res
}

type TestInput struct {
    Args []interface{} `json:"args"`
    Expected interface{} `json:"expected"`
    Id int `json:"id"`
}

type TestOutput struct {
    Id int              `json:"id"`
    Success bool        `json:"success"`
    Result interface{}  `json:"result"`
    Elapse float64      `json:"elapse"`
}

func convByType(untyped interface{}, rtype reflect.Type) reflect.Value {
    content, _ := json.Marshal(untyped)
    v := reflect.New(rtype)
    p := v.Interface()
    json.Unmarshal(content, p)
    return v.Elem()
}

func main() {
    input := unittest.ReadStdin()
    testInput := TestInput {}
    if err := json.Unmarshal([]byte(input), &testInput); err != nil {
        fmt.Fprintf(os.Stderr, "JSON unmarshaling failed: %s", err)
        return
    }

    function := reflect.ValueOf(buildString)
    args := make([]reflect.Value, function.Type().NumIn())
    for i := 0; i < len(testInput.Args); i++ {
        args[i] = convByType(testInput.Args[i], function.Type().In(i))
    }
    rs := function.Call(args)
    res := rs[0].Interface()
    fmt.Fprintf(os.Stderr, "%v\n", res)

    // arg0, _ := json.Marshal(testInput.Args[0])
    // _strs := []string {}
    // _type := reflect.TypeOf(_strs)
    // _v := reflect.New(_type)
    // newP := _v.Interface()
    // json.Unmarshal(arg0, newP)
    // fmt.Fprintf(os.Stderr, "%+v\n", newP)

//    fmt.Fprintf(os.Stderr, "<< %v >>", reflect.ValueOf(testInput.Args[0]).Kind())
//    res := buildString(testInput.Args[0].([]string), testInput.Args[1].([]int))
//    fmt.Fprintf(os.Stderr, "%v", testInput)
//    fmt.Fprintf(os.Stderr, "%v", res)

    out := TestOutput {}
    out.Id = testInput.Id
    out.Success = true
    out.Result = res
    out.Elapse = 0.023
    jstring, err := json.Marshal(out)
    if err != nil {
        fmt.Fprintf(os.Stderr, "JSON marshaling failed: %s", err)
        return
    }
    fmt.Print(string(jstring))
}
