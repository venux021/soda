#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def do_cal(arr, i, j, temp):
    if i == j:
        return 0

    mid = (i + j)/2
    return do_cal(arr, i, mid, temp) + do_cal(arr, mid + 1, j, temp) + merge(arr, i, mid, j, temp)

def merge(arr, i, mid, j, temp):
    a = i
    b = mid + 1
    c = i
    s = 0
    while a <= mid and b <= j:
        if arr[a] <= arr[b]:
            s += (arr[a] * (j-b+1))
            temp[c] = arr[a]
            a += 1
            c += 1
        else:
            temp[c] = arr[b]
            b += 1
            c += 1
    while a <= mid:
        temp[c] = arr[a]
        a += 1
        c += 1
    while b <= j:
        temp[c] = arr[b]
        b += 1
        c += 1

    arr[i:j+1] = temp[i:j+1]

    return s

def small_sum(arr):
    n = len(arr)
    temp = [0] * n
    return do_cal(arr, 0, n-1, temp)

def test(arr):
    print 'arr: {}'.format(arr)
    print 'small sum: {}'.format(small_sum(arr))

def main():
    '''计算数组的小和'''
    test([1,3,5,2,4,6])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
