#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def find_dual(arr, k):
    n = len(arr)
    i, j = 0, n-1
    r = []
    while i < j:
        if arr[i] + arr[j] == k:
            r.append((arr[i], arr[j]))
            i += 1
            j -= 1
        elif arr[i] + arr[j] > k:
            j -= 1
        else:
            i += 1
    return r

@testwrapper
def test(arr, k):
    print(arr, k)
    print(find_dual(arr, k))

def main():
    test([-8,-4,-3,0,1,2,4,5,8,9], 10)
    test([-8,-4,-3,0,1,2,4,5,8,9], 9)
    test([-8,-4,-3,0,1,2,4,5,8,9], 17)
    test([-8,-4,-3,0,1,2,4,5,8,9], 18)

if __name__ == '__main__':
    main()
