#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def need_sort(arr):
    n = len(arr)
    _min = arr[n-1]
    left = -1
    for i in range(n-2, -1, -1):
        if arr[i] > _min:
            left = i
        _min = min(_min, arr[i])

    if left == -1:
        return 0

    _max = arr[0]
    right = -1
    for i in range(1, n):
        if arr[i] < _max:
            right = i
        _max = max(_max, arr[i])

    return right - left + 1

def test(arr):
    print 'arr: {}'.format(arr)
    print 'len: {}'.format(need_sort(arr))

def main():
    '''需要排序的最短子数组长度'''
    test([1,5,3,4,2,6,7])
    test([1,2,3,4,5,6,7])
    test([7,6,5,4,3,2,1])
    test([7,6,5,4,3,1,2])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
