#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def max_sub(arr, k):
    n = len(arr)
    if n == 0:
        return []

    i = j = 0
    s = arr[0]
    max_len = 0
    sub_arr = []
    while j < n:
        if s == k:
            if j-i+1 > max_len:
                max_len = j-i+1
                sub_arr = arr[i:j+1]
            s -= arr[i]
            i += 1
            j += 1
            if j < n:
                s += arr[j]
        elif s < k:
            j += 1
            if j < n:
                s += arr[j]
        elif i < j:
            s -= arr[i]
            i += 1
        else:
            s -= arr[i]
            i += 1
            j += 1
            if j < n:
                s += arr[j]
    return sub_arr

def test(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    print 'sub: {}'.format(max_sub(arr, k))

def main():
    '''未排序正数数组中累加和为给定值的最长子数组长度'''
    test([4,2,1,1,1], 3)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
