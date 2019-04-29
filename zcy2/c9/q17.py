#!/usr/bin/env python3
import random
import sys

from sodacomm.tools import testwrapper

def select_by_m(arr, m):
    n = len(arr)
    if m >= n:
        return list(arr)

    buf = []
    for i in range(n, n-m, -1):
        j = int(random.random() * i)
        buf.append(arr[j])
        arr[j], arr[i-1] = arr[i-1], arr[j]

    return buf

@testwrapper
def test(arr, m):
    print(arr, m)
    print(select_by_m(arr, m))

def main():
    test([1,2,3,4,5], 1)
    test([1,2,3,4,5], 5)
    test([1,2,3,4,5], 3)
    test([1,2,3,4,5,9,8,7,6,0], 6)

if __name__ == '__main__':
    main()
