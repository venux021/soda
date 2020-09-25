#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def find_min_old(arr):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] <= arr[low] and arr[mid] <= arr[high]:
            return arr[mid]
        elif arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid - 1

def find_min(arr):
    n = len(arr)
    low = 0
    high = n - 1
    while low < high:
        if low == high - 1:
            break
        if arr[low] < arr[high]:
            return arr[low]
        else:
            mid = (low + high) / 2
            if arr[mid] < arr[low]:
                high = mid
            elif arr[mid] > arr[high]:
                low = mid
            else:
                while low < mid and arr[low] == arr[mid]:
                    low += 1
                if arr[low] > arr[mid]:
                    high = mid
    return min(arr[low], arr[high])

def test(arr):
    print 'arr: {}'.format(arr)
    print 'min: {}'.format(find_min(arr))

def main():
    '''在有序旋转数组中找到最小值'''
    test([1,2,3,4,5,6,7])
    test([4,5,6,7,1,2,3])
    test([5,6,7,1,2,3,4])
    test([2,2,1,2,2,2,2])
    test([2,3,2,2,2,2,2])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
