package main

import "soda/unittest"

func TEST_ADD(a int, b int) int {
    return a + b
}

func main() {
    work := unittest.CreateWork(TEST_ADD)
    // work.SetValidator(func(e,r)bool)
    work.CompareSerial = true
    // work.SetArgParser(index, func(s)a)
    // work.SetResultParser(func(s)w)
    // work.SetResultSerializer(func(w)s)
    work.Run()
}
