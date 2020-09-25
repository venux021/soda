#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def partition(arr, i, j):
    if i == j:
        return i

    mid = (i+j) >> 1
    t = arr[i]
    arr[i] = arr[mid]
    arr[mid] = t

    k = arr[i]
    while i < j:
        while i < j and arr[j] >= k:
            j -= 1
        if i < j:
            arr[i] = arr[j]

        while i < j and arr[i] < k:
            i += 1
        if i < j:
            arr[j] = arr[i]

    arr[i] = k
    return i

def more_than_half(arr):
    n = len(arr)
    low = 0
    high = n - 1
    mid = (n-1) >> 1
    while low <= high:
        pt = partition(arr, low, high)
        if pt == mid:
            low = mid
            break
        elif pt < mid:
            low = pt + 1
        else:
            high = pt - 1

    k = arr[low]

    if test_more_than_half(arr, k):
        return k

def test_more_than_half(arr, k):
    c = 0
    for v in arr:
        if v == k:
            c += 1
    return c > len(arr) // 2

def more_than_half2(arr):
    n = len(arr)
    cand = None
    c = 0
    for v in arr:
        if c == 0:
            cand = v
            c = 1
        elif cand == v:
            c += 1
        else:
            c -= 1

    if test_more_than_half(arr, cand):
        return cand

def test(arr):
    print('arr: {}'.format(arr))
    print('more than half 1: {}'.format(more_than_half(arr)))
    print('more than half 2: {}'.format(more_than_half2(arr)))
    print('----')

def main():
    '''数组中出现次数超过一半的数字'''
    test([1,2,3,2,2,2,5,4,2])
    test([1,2,3,2,2,2,5,2,4,2])
    test([1,2,3,4,5,6,7,8])
    test([1,2,3,4,5,6,7])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
