#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

def find_min_max(arr):
    n = len(arr)
    if n & 1:
        mn = mx = arr[0]
        i = 1
    else:
        if arr[0] > arr[1]:
            mn = arr[1]
            mx = arr[0]
        else:
            mn = arr[0]
            mx = arr[1]
        i = 2

    while i < n:
        a, b = arr[i], arr[i+1]
        if a > b:
            mn = min(mn, b)
            mx = max(mx, a)
        else:
            mn = min(mn, a)
            mx = max(mx, b)
        i += 2

    return (mn, mx)

def test(n):
    arr = [random.randint(1,100) for i in range(n)]
    print('origin:', arr)
    mn, mx = find_min_max(arr)
    print('min: {}, max: {}'.format(mn, mx))

def main():
    '''同时找出最小值和最大值'''
    test(2)
    test(3)
    test(10)
    test(11)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
