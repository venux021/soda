#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def max_sub_len(arr, k):
    n = len(arr)
    s = 0
    _sum = [0] * n
    len2i = {0: -1}
    for i in range(n):
        s += arr[i]
        _sum[i] = s
        if s not in len2i:
            len2i[s] = i

    max_len = 0
    for i in range(n):
        L = _sum[i] - k
        if L in len2i:
            max_len = max(max_len, i - len2i[L])

    return max_len

def test(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    print 'max sub len: {}'.format(max_sub_len(arr, k))

def test2(arr):
    print 'arr: {}'.format(arr)
    print 'max sub len: {}'.format(max_sub_len2(arr))

def max_sub_len2(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1
    r = max_sub_len(arr, 0)
    for i in range(n):
        if arr[i] == -1:
            arr[i] = 0
    return r

def main():
    '''未排序数组中累加和为给定值的最长子数组系列问题'''
    test([1,2,3,3], 6)
    test([-4,6,3,-5,0,2,9,0,0,-7,-10,3,-8,-5,8,2], 5)
    test([0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,1,1,0], 5)
    test2([0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,1,1,0])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
