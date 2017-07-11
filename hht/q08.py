#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def find_min(arr):
    n = len(arr)
    i = 0
    j = n - 1
    while i <= j:
        mid = (i+j) // 2
        if arr[i] != arr[j]:
            if arr[mid] >= arr[i] and arr[mid] >= arr[j]:
                i = mid + 1
            else:
                j = mid
        elif arr[mid] > arr[i]:
            i = mid + 1
        elif arr[mid] < arr[i]:
            j = mid
        else:
            while i < mid and arr[i] == arr[mid]:
                i += 1
            if i < mid and arr[i] > arr[mid]:
                j = mid
            elif i < mid and arr[i] < arr[mid]:
                return arr[i]
            else:
                i = mid + 1
    return arr[j]

def test(arr):
    print('arr:', arr)
    print('min:', find_min(arr))

def main():
    '''旋转数组的最小数字'''
    test([3,4,5,1,2])
    test([5,6,7,1,2,3,4])
    test([2,2,1,2,2,2,2,2])
    test([2,2,2,2,2,1,2])
    test([2,2,2,2,2,2,2])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
