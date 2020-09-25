#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def accumulate_other(arr):
    n = len(arr)
    result = [0] * n
    t = 1
    for v in arr:
        t *= v
    for i in range(n):
        result[i] = t // arr[i]
    return result

def accumu_2(arr):
    n = len(arr)
    L = [0] * n
    R = [0] * n
    t = 1
    for i in range(n):
        t *= arr[i]
        L[i] = t
    t = 1
    for i in range(n-1, -1, -1):
        t *= arr[i]
        R[i] = t

    result = [0] * n
    result[0] = R[1]
    result[n-1] = L[n-2]
    for i in range(1, n-1):
        result[i] = L[i-1] * R[i+1]

    return result

@testwrapper
def test(arr):
    print(arr)
    print(accumulate_other(arr))
    print(accumu_2(arr))

def main():
    test([2,3,1,4])

if __name__ == '__main__':
    main()
