#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def first_miss(arr):
    n = len(arr)
    first = min(arr)
    p = 0
    r = n

    while p < r:
        if arr[p] == p + first:
            p += 1
        elif arr[p] > p + first and arr[p] < r + first:
            q = arr[p] - first
            t = arr[q]
            arr[q] = arr[p]
            arr[p] = t
        else:
            r -= 1
            t = arr[p]
            arr[p] = arr[r]
            arr[r] = t
    return p + first

def test(arr):
    print 'arr: {}'.format(arr)
    print 'first miss: {}'.format(first_miss(arr))

def main():
    '''数组的第一个不连续数'''
    test([1,2,3,4])
    test([-1,2,3,4])
    test([2,5,3,4,1,-1,0,7,10,9,8])
    test([2])
    test([-3])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
