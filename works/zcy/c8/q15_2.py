#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def adjusted(arr):
    n = len(arr)
    od = 1
    ev = 0
    while od < n and ev < n:
        if arr[-1] & 1 == 0:
            swap(arr, -1, ev)
            ev += 2
        else:
            swap(arr, -1, od)
            od += 2
    return arr

def test(arr):
    print 'arr: {}'.format(arr)
    print 'adjusted: {}'.format(adjusted(arr))

def main():
    '''奇数下标都是奇数或者偶数下标都是偶数'''
    test([3,7,9,2,6,2,8,1,5,8,3,6,4])
    test([10,7,4,2,6,2,8,1,6,8,3,6,4])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
