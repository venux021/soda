#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def do_partition(arr):
    n = len(arr)
    u = 0
    i = 1
    while i < n:
        if arr[i] != arr[u]:
            if u + 1 < i:
                arr[u+1], arr[i] = arr[i], arr[u+1]
            u += 1
        i += 1

@testwrapper
def test(arr):
    print(arr)
    do_partition(arr)
    print(arr)

def sort_012(arr):
    n = len(arr)
    a = -1
    b = n
    i = 0
    while i < b:
        if arr[i] == 1:
            i += 1
        elif arr[i] == 0:
            if a + 1 < i:
                arr[a+1] = 0
                arr[i] = 1
            i += 1
            a += 1
        else:
            arr[b-1], arr[i] = arr[i], arr[b-1]
            b -= 1

@testwrapper
def test2(arr):
    print(arr)
    sort_012(arr)
    print(arr)

def k_partition(arr, k):
    n = len(arr)
    left = -1
    right = n
    i = 0
    while i < right:
        if arr[i] == k:
            i += 1
        elif arr[i] < k:
            arr[i], arr[left+1] = arr[left+1], arr[i]
            left += 1
            i += 1
        else:
            arr[i], arr[right-1] = arr[right-1], arr[i]
            right -= 1

@testwrapper
def test3(arr, k):
    print(arr, k)
    k_partition(arr, k)
    print(arr)

def main():
    test([1,2,2,2,3,3,4,5,6,6,7,7,8,8,8,9])
    test2([1,2,2,0,0,1,1,2,1,2,0,1,2,0,0,1,1,2,1])
    test2([0,2,2,0,0,1,1,2,1,2,0,1,2,0,0,1,1,2,2])
    test2([0,2,2,0,0,2,2,0,2,0,0,2,2])
    test2([1,2,2,2,1])
    test2([1,0,0,1,0,1])
    test3([3,7,4,2,1,8,9,4,5,4,0], 4)

if __name__ == '__main__':
    main()
