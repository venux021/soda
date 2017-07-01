#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def max_sub_len(arr, k):
    n = len(arr)
    s = 0
    _sum = [0] * n
    for i in range(n):
        s += arr[i]
        _sum[i] = s

    left_max = [0] * n
    left_max[0] = arr[0]
    for i in range(1, n):
        if arr[i] > left_max[i-1]:
            left_max[i] = arr[i]

    max_len = 0
    for i in range(n):
        if _sum[i] <= k:
            sub_len = i + 1
        else:
            d = _sum[i] - k
            low = 0
            high = n-1
            while low <= high:
                mid = (low + high) / 2
                if left_max[mid] >= d:
                    high = mid - 1
                else:
                    low = mid + 1
            sub_len = 0 if low >= n else i - low + 1
        max_len = max(max_len, sub_len)

    return max_len

def test(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    print 'max sub len: {}'.format(max_sub_len(arr, k))

def main():
    '''未排序数组中累加和小于或等于给定值的最长子数组长度'''
    test([3,-2,-4,0,6], -2)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
