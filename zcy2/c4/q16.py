#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def longest_consecutive(arr):
    n = len(arr)
    m = {}
    max_len = 0
    for v in arr:
        if v in m:
            continue
        m[v] = 1
        if v - 1 in m:
            L = m[v-1]
            left = v - L
            m[left] = m[v] = L + 1
            max_len = max(max_len, L + 1)
        if v + 1 in m:
            R = m[v+1]
            right = v + R
            new_len = R + m[v]
            m[right] = m[right-new_len+1] = new_len
            max_len = max(max_len, new_len)
    return max_len

@testwrapper
def test(arr):
    print(arr)
    print(longest_consecutive(arr))

def main():
    test([100,4,200,1,3,2])
    test([-3,2,4,10,7,9,3,1,-2,-1,-1,2,4,10,0])

if __name__ == '__main__':
    main()
