#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def longest_sub_size(arr):
    n = len(arr)
    size = 0
    for i in range(n):
        _min = sys.maxsize
        _max = -_min
        s = set()
        for j in range(i, n):
            if arr[j] in s:
                break
            s.add(arr[j])
            _max = max(_max, arr[j])
            _min = min(_min, arr[j])
            if _max - _min == j - i:
                size = max(size, j - i + 1)
    return size

@testwrapper
def test(arr):
    print(arr)
    print(longest_sub_size(arr))

def main():
    test([5,5,3,2,6,4,3])

if __name__ == '__main__':
    main()
