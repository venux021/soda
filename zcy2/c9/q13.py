#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def to_stat(arr):
    path_to_dist(arr)
    
    for i in range(len(arr)):
        if arr[i] >= 0:
            continue
        j = -arr[i]
        arr[i] = 0
        while arr[j] < 0:
            target = arr[j]
            arr[j] = 1
            j = -target
        arr[j] += 1
    arr[0] = 1

def path_to_dist(arr):
    n = len(arr)
    cap = -1
    for i in range(n):
        if arr[i] < 0:
            continue
        elif arr[i] == i:
            cap = i
            continue
        last = -1
        j = i
        while arr[j] != j and arr[j] >= 0:
            nx = arr[j]
            arr[j] = last
            last = j
            j = nx
        dist = -1 if arr[j] == j else arr[j] - 1
        j = last
        while j >= 0:
            nx = arr[j]
            arr[j] = dist
            dist -= 1
            j = nx
    arr[cap] = 0

@testwrapper
def test(arr):
    print(arr)
    to_stat(arr)
    print(arr)

def main():
    test([9,1,4,9,0,4,8,9,0,1])

if __name__ == '__main__':
    main()
