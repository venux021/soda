#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def local_min(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] < arr[1]:
        return 0
    if arr[n-1] < arr[n-2]:
        return n-1
    for i in range(1, n-1):
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            return i
    return -1

def local_min2(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] < arr[1]:
        return 0
    if arr[n-1] < arr[n-2]:
        return n-1
    L = 1
    R = n-2
    while L < R:
        mid = (L + R) // 2
        if arr[mid] > arr[mid-1]:
            R = mid - 1
        elif arr[mid] > arr[mid+1]:
            L = mid + 1
        else:
            return mid
    return L

@testwrapper
def test(arr):
    print(arr)
    print(local_min(arr))
    print(local_min2(arr))

def main():
    test([13,12,5,4,9,10])
    test([10,1,2,9])
    test([10,3,2,9])

if __name__ == '__main__':
    main()
