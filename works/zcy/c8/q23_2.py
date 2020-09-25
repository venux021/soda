#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def partition(arr):
    n = len(arr)
    i = 0
    j = 1
    while j < n:
        if arr[j] > arr[i]:
            i += 1
            if i < j:
                swap(arr, i, j)
        j += 1
    return arr

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def test(arr):
    print 'arr: {}'.format(arr)
    print 'partition: {}'.format(partition(arr))

def pt012(arr, low, high, k):
    i = j = low
    while j <= high:
        if arr[j] < k:
            if i < j:
                swap(arr, i, j)
            i += 1
        j += 1
    return i

def partition_012(arr):
    n = len(arr)
    i = pt012(arr, 0, n-1, 1)
    pt012(arr, i, n-1, 2)
    return arr

def test2(arr):
    print 'arr: {}'.format(arr)
    print 'partition: {}'.format(partition_012(arr))

def pt3(arr, k):
    n = len(arr)
    i = pt012(arr, 0, n-1, k)
    pt012(arr, i, n-1, k+1)
    return arr

def test3(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    print 'partition: {}'.format(pt3(arr, k))

def main():
    '''数组的partition调整'''
    test([1,2,2,2,3,3,4,5,6,6,7,7,8,8,8,9])
    test2([0,2,2,1,1,0,0,2,1,2,1,1,2,2,0,1,2,2,1,2,1,0])
    test3([1,3,6,2,3,8,5,2,4,3,1,5,9,6,7,8,2,3,4,9,5,2,1,6,5], 5)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
