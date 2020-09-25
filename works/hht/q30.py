#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def smallest_k(arr, k):
    n = len(arr)
    low = 0
    high = n - 1
    m = k - 1
    while low <= high:
        p = partition(arr, low, high)
        if p == m:
            low = p
            break
        elif p > m:
            high = p - 1
        else:
            low = p + 1
    return arr[:k]

def partition(arr, i, j):
    if i == j:
        return i
    k = (i+j) >> 1
    p = arr[k]
    arr[k] = arr[i]
    while i < j:
        while i < j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i] = arr[j]
        while i < j and arr[i] < p:
            i += 1
        if i < j:
            arr[j] = arr[i]
    arr[i] = p
    return i

def test(arr, k):
    print('arr: {}, k: {}'.format(arr, k))
    print('smallest k: {}'.format(smallest_k(arr, k)))

def main():
    '''最小的k个数'''
    test([4,5,1,6,2,7,3,8], 1)
    test([4,5,1,6,2,7,3,8], 3)
    test([4,5,1,6,2,7,3,8], 7)
    test([4,5,1,6,2,7,3,8], 8)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
