#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def times(arr, k):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) >> 1
        if arr[mid] >= k:
            high = mid - 1
        else:
            low = mid + 1
    left = low

    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) >> 1
        if arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    right = low
    return right - left

def test(arr, k):
    print('arr: {}, k: {}'.format(arr, k))
    print('times: {}'.format(times(arr, k)))

def main():
    '''数字在排序数组中出现的次数'''
    test([1,2,3,3,3,3,4,5], 3)
    test([1,2,3,4,5], 3)
    test([1,2,4,5], 3)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
