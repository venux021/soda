#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def tell_nth(arr):
    F, M, T = 1, 2, 3
    n = len(arr)
    step = 0
    for i in range(n, 0, -1):
        v = arr[i-1]
        if v == M:
            return -1
        elif v == T:
            step += (1 << (i-1))
            F, M = M, F
        else:
            M, T = T, M
    return step

@testwrapper
def test(arr):
    print(arr, tell_nth(arr))

def main():
    test([1,1])
    test([2,1])
    test([3,3])
    test([2,2])

if __name__ == '__main__':
    main()
