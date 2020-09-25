#!/usr/bin/env python3
import math
import sys

from sodacomm.tools import testwrapper

def max_gap(arr):
    n = len(arr)
    _min = min(arr)
    _max = max(arr)
    bsize = (_max - _min) / n
    buckets = [None] * (n+1)
    for v in arr:
        if v == _max:
            buckets[-1] = (_max, _max)
        else:
            i = int((v - _min) / bsize)
            if not buckets[i]:
                buckets[i] = (v, v)
            else:
                b = buckets[i]
                buckets[i] = (min(b[0],v), max(b[1],v))

    gap = 0
    last = -1
    for i in range(n+1):
        if buckets[i] is None:
            continue
        if last != -1:
            gap = max(gap, buckets[i][0] - buckets[last][1])
        last = i

    return gap

@testwrapper
def test(arr):
    print(arr)
    print(max_gap(arr))

def main():
    test([9,3,1,10])
    test([5,5,5,5])
    test([3,-2])

if __name__ == '__main__':
    main()
