package main

import _ "soda/leetcode"
import "soda/unittest"

func main() {
    work := unittest.CreateWork(FUNCTION)
    // work.SetValidator(func(e,r)bool)
    work.CompareSerial = true
    // work.SetArgParser(index, func(s)a)
    // work.SetResultParser(func(s)w)
    // work.SetResultSerializer(func(w)s)
    work.Run()
}
