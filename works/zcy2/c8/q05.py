#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def min_len_need_sort(arr):
    i = -1
    n = len(arr)
    m = arr[n-1]
    for j in range(n-2, -1, -1):
        if arr[j] > m:
            i = j
        else:
            m = min(m, arr[j])
    if i == -1:
        return 0

    p = -1
    m = arr[0]
    for j in range(1, n):
        if arr[j] < m:
            p = j
        else:
            m = max(m, arr[j])
    return p - i + 1

@testwrapper
def test(arr):
    print(arr)
    print(min_len_need_sort(arr))

def main():
    test([1,5,3,4,2,6,7])
    test([7,6,5,4,3,2,1])
    test([1,2,3,4,5,6,7])
    test([1,2,3,5,4,6,7])

if __name__ == '__main__':
    main()
