#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def max_multiple(arr):
    n = len(arr)
    _max = -sys.maxsize
    mx = mn = 1
    for v in arr:
        mx *= v
        mn *= v
        _max = max(_max, v, mx, mn)
        if v == 0:
            mx = mn = 1
    return _max

@testwrapper
def test(arr):
    print(arr)
    print(max_multiple(arr))

def main():
    test([-2.5,4,0,3,0.5,8,-1])
    test([-2.5,4,0,-3,0.5,8,1])

if __name__ == '__main__':
    main()
