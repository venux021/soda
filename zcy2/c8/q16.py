#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def max_sum(arr):
    k = get_max(arr)
    if k < 0:
        return k
    n = len(arr)
    cur = 0
    i = 0
    _max = 0
    for v in arr:
        cur += v
        if cur < 0:
            cur = 0
        else:
            _max = max(_max, cur)
    return _max

def get_max(arr):
    _max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > _max:
            _max = arr[i]
    return _max

@testwrapper
def test(arr):
    print(arr)
    print(max_sum(arr))

def main():
    test([1,-2,3,5,-2,6,-1])

if __name__ == '__main__':
    main()
