package main

import "soda/unittest"

func TEST_ADD(a int, b int) int {
    return a + b
}

func main() {
    work := unittest.CreateWork(TEST_ADD)
    work.CompareSerial = true
    // work.SetArgParser(index, FUNC(a))
    // work.SetValidator(FUNC(e,r))
    // work.SetResultParser(FUNC(r))
    // work.SetResultSerializer(FUNC(s))
    work.Run()
}
