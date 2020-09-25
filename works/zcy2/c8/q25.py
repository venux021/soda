#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def miss_num(arr):
    n = len(arr)
    L = 0
    R = n
    while L < R:
        if arr[L] == L + 1:
            L += 1
        elif arr[L] <= L or arr[L] > R or arr[arr[L]-1] == arr[L]:
            R -= 1
            arr[L] = arr[R]
        else:
            k = arr[L]
            arr[L], arr[k-1] = arr[k-1], arr[L]
    return L + 1

@testwrapper
def test(arr):
    print(arr)
    print(miss_num(arr))

def main():
    test([-1,2,3,4])
    test([1,2,3,4])
    test([9,10,5,6,7,1,2,3])

if __name__ == '__main__':
    main()
