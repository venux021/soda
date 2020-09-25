#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import shuffle
import sys

def par_min(arr):
    n = len(arr)
    if n == 0:
        return -1
    elif n == 1 or arr[0] < arr[1]:
        return 0
    elif arr[n-2] > arr[n-1]:
        return n-1

    left = 1
    right = n-2
    while left < right:
        mid = (left + right) / 2
        if arr[mid] > arr[mid-1]:
            right = mid-1
        elif arr[mid] > arr[mid+1]:
            left = mid+1
        else:
            return mid
    return left

def test(arr):
    print 'arr: {}'.format(arr)
    print 'partial min: {}'.format(par_min(arr))

def main():
    '''在数组中找到一个局部最小的位置'''
    a = list(range(10))
    shuffle(a)
    test(a)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
