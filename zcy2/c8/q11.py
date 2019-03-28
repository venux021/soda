#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def longest_sub_seq(arr, k):
    v2i = {0:-1}
    s = 0
    _len = 0
    for i, v in enumerate(arr):
        s += v
        v2i.setdefault(s, i)
        j = v2i.get(s - k, i)
        _len = max(_len, i-j)
    return _len

def longest_sub_pn(arr):
    def conv(v):
        if v > 0:
            return 1
        elif v < 0:
            return -1
        else:
            return v
    return longest_sub_seq(list(map(conv, arr)), 0)

def longest_sub_01(arr):
    a2 = [i if i == 1 else -1 for i in arr]
    return longest_sub_seq(a2, 0)

@testwrapper
def test1(arr, k):
    print(arr, k)
    print(longest_sub_seq(arr, k))
    print(longest_sub_pn(arr))

@testwrapper
def test2(arr):
    print(arr)
    print(longest_sub_01(arr))

def main():
    test1([-1,3,9,-2,5,4,-3,0,7,2], 4)
    test1([-1,3,9,-2,5,4,-3,0,7,2], 9)
    test1([1,2,3,3], 6)
    test2([1,0,0,1,0,0,1,0,0,0])

if __name__ == '__main__':
    main()
