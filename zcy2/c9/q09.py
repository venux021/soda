#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def max_abs1(arr):
    n = len(arr)
    if n <= 1:
        return 0
    stk = [arr[-1]]
    for i in range(n-2, 0, -1):
        if arr[i] >= stk[-1]:
            stk.append(arr[i])

    left_max = arr[0]
    k = 0
    res = 0
    while k < n-1:
        right_max = stk[-1]
        res = max(res, abs(right_max - left_max))
        k += 1
        left_max = max(arr[k], left_max)
        if arr[k] == stk[-1]:
            stk.pop()
    return res

def max_abs2(arr):
    mx = max(arr)
    return max(abs(mx - arr[0]), abs(mx - arr[-1]))

@testwrapper
def test(arr):
    print(arr)
    print(max_abs1(arr))
    print(max_abs2(arr))

def main():
    test([2,7,3,1,1])

if __name__ == '__main__':
    main()
