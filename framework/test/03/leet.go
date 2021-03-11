package main

import _ "soda/leetcode"
import "soda/unittest"

type Input1 struct {
    Value int
}

type Input2 struct {
    Text string
}

type Output struct {
    Val int
    Str string
}

func gen(i1 Input1, i2 *Input2) Output {
    return Output{i1.Value, i2.Text}
}

func main() {
    work := unittest.CreateWork(gen)
    work.SetValidator(func(e, r Output)bool {
        return e.Val == r.Val && e.Str == r.Str
    })
    // work.CompareSerial = true
    work.SetArgParser(0, func(i int) Input1 { return Input1{i} })
    work.SetArgParser(1, func(t string) *Input2 { return &Input2{t} })
    work.SetResultParser(func(s []string) Output { return Output{len(s), s[0]} })
    work.SetResultSerializer(func(r Output) []string {
        var s []string
        for i := 0; i < r.Val; i++ {
            s = append(s, r.Str)
        }
        return s
    })
    work.Run()
}
