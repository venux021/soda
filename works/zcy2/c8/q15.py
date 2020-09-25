#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def even_odd(arr):
    n = len(arr)
    i = 0
    while i < n:
        a = i % 2
        b = arr[i] % 2
        if a == b:
            i += 1
        elif i < n-1:
            tmp = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = tmp
            i += 2
        else:
            break

@testwrapper
def test(arr):
    print(arr)
    even_odd(arr)
    print(arr)

def main():
    test([4,1,2,6,3,5,8,9,7])

if __name__ == '__main__':
    main()
