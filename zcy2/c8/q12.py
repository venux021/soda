#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def longest_sub_seq(arr, k):
    n = len(arr)
    sums = [0] * (n+1)
    t = 0
    for i, v in enumerate(arr):
        t += v
        sums[i+1] = t

    es = [0] * (n+1)
    _m = 0
    for i, v in enumerate(sums):
        if v > _m:
            _m = v
        es[i] = _m

    _len = 0
    for i in range(1, n+1):
        p = sums[i] - k
        j = dofind(es, i-1, p)
        if j != -1:
            _len = max(_len, i - j)

    return _len

def dofind(es, j, num):
    low = 0
    high = j
    while low <= high:
        mid = (low + high) // 2
        if es[mid] >= num:
            high = mid - 1
        else:
            low = mid + 1
    return low if low <= j else -1

@testwrapper
def test(arr, k):
    print(arr, k)
    print(longest_sub_seq(arr, k))

def main():
    test([1,2,0,-1,0,5,-2], 3)
    test([3,-2,-4,0,6], -2)
    test([3,-2,-4,0,0,0,6], -2)

if __name__ == '__main__':
    main()
