#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def odd_occur(arr):
    k = 0
    for c in arr:
        k ^= c
    return k

def odd_occur2(arr):
    k = 0
    for c in arr:
        k ^= c
    mask = k & (~k + 1)
    p = 0
    for c in arr:
        if c & mask:
            p ^= c
    return (p, p ^ k)

@testwrapper
def test(arr):
    print(arr)
    print(odd_occur(arr))

@testwrapper
def test2(arr):
    print(arr)
    print(odd_occur2(arr))

def main():
    test([1,2,1,2,2,3,4,3,4])
    test([0,0,0,1,1,2,2])
    test2([1,3,0,0,9,9,4,4,4,4,2,2])
    test2([5,6,0,7,8,8,1,1,1,7,6,5])

if __name__ == '__main__':
    main()
