#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def missing_positive_int(arr):
    L = 0
    R = len(arr)
    while L < R:
        if arr[L] == L + 1:
            L += 1
        elif arr[L] > R or arr[L] <= L or arr[arr[L]-1] == arr[L]:
            R -= 1
            arr[R], arr[L] = arr[L], arr[R]
        else:
            k = arr[L] - 1
            arr[k], arr[L] = arr[L], arr[k]
    return L + 1

@testwrapper
def test(arr):
    print(arr)
    print(missing_positive_int(arr))

def main():
    test([-1,2,3,4])
    test([1,2,3,4])
    test([9,10,5,6,7,1,2,3])
    test([1,2,0])
    test([3,4,-1,1])
    test([7,8,9,11,12])
    test([2])
    test([1])
    test([0])

if __name__ == '__main__':
    main()
