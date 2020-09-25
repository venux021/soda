#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def sort_n(arr):
    n = len(arr)
    p = 0
    while p < n:
        q = arr[p]
        while arr[p] != p + 1:
            tmp = arr[q-1]
            arr[q-1] = q
            q = tmp
        p += 1

@testwrapper
def test(arr):
    print(arr)
    sort_n(arr)
    print(arr)

def main():
    test([5,1,3,7,4,2,9,8,6])
    test([8,7,6,5,4,3,2,1])
    test([1,2,3,4,5,6,7,8])
    test([1,3,5,7,9,2,4,6,8,10])

if __name__ == '__main__':
    main()
