#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def found(arr, k):
    n = len(arr)
    low = 0
    high = n - 1
    num = k
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == k:
            return mid

        if arr[mid] == arr[low] and arr[mid] == arr[high]:
            while mid != low and arr[mid] == arr[low]:
                low += 1
            if mid == low:
                low = mid + 1
                continue

        if arr[mid] != arr[low]:
            if arr[mid] > arr[low]:
                if num >= arr[low] and num < arr[mid]:
                    high -= 1
                else:
                    low += 1
            else:
                if num > arr[mid] and num <= arr[high]:
                    low += 1
                else:
                    high -= 1
        else:
            if arr[mid] < arr[high]:
                if num > arr[mid] and num <= arr[high]:
                    low += 1
                else:
                    high -= 1
            else:
                if num >= arr[low] and num < arr[mid]:
                    high -= 1
                else:
                    low += 1

    return -1

def test(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    print 'result: {}'.format(found(arr, k))

def main():
    '''在有序旋转数组中找到一个数'''
    test([1,2,3,4,5,6,7], 3)
    test([1,2,3,4,5,6,7], 1)
    test([1,2,3,4,5,6,7], 7)
    test([1,2,3,4,5,6,7], -1)
    test([1,2,3,4,5,6,7], 8)
    test([4,5,6,7,1,2,3], 3)
    test([4,5,6,7,1,2,3], 1)
    test([4,5,6,7,1,2,3], 7)
    test([4,5,6,7,1,2,3], -1)
    test([4,5,6,7,1,2,3], 8)
    test([7,7,7,7,7,5,7], 5)
    test([7,5,7,7,7,7,7], 5)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
