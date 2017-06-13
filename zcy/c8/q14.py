#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import shuffle
import sys

def sort(arr):
    n = len(arr)
    for i in range(n):
        j = i + 1
        p = arr[i]
        if p != j:
            while p != j:
                t = arr[p-1]
                arr[p-1] = p
                p = t
            arr[i] = p

def test(arr):
    shuffle(arr)
    print 'arr: {}'.format(arr)
    sort(arr)
    print 'sorted: {}'.format(arr)

def main():
    '''自然数数组的排序'''
    test([1,2,3,4,5,6,7,8,9,10])


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
