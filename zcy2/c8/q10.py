#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def longest_sub_seq(arr, k):
    n = len(arr)
    i = 0
    j = -1
    t = 0
    max_size = 0
    while True:
        if j < i or t < k:
            j += 1
            if j == n:
                break
            t += arr[j]
        else:
            if t == k:
                max_size = max(max_size, j-i+1)
            t -= arr[i]
            i += 1
    return max_size

@testwrapper
def test(arr, k):
    print(arr, k)
    print(longest_sub_seq(arr, k))

def main():
    test([1,2,1,1,1], 3)
    test([1,2,1,1,1,1], 4)
    test([1,2,1,1,1], 2)
    test([1,2,1,1,1], 10)

if __name__ == '__main__':
    main()
