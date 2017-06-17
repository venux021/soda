#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def first_miss(arr):
    n = len(arr)
    i = 0
    j = n
    while i < j:
        if arr[i] == i + 1:
            i += 1
        elif arr[i] <= i or arr[i] > n or arr[arr[i]-1] == arr[i]:
            j -= 1
            arr[i] = arr[j]
        else:
            k = arr[i] - 1
            t = arr[k]
            arr[k] = arr[i]
            arr[i] = t
    return i + 1

def test(arr):
    print 'arr: {}'.format(arr)
    print 'first miss: {}'.format(first_miss(arr))

def main():
    '''数组中未出现的最小正整数'''
    test([-1,2,3,4])
    test([1,2,3,4])
    test([2,5, 3, 4, 1, -1, 0, 7, 10, 9, 8])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
