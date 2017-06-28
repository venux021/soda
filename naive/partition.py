#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

def parttn(arr, k):
    i = 0
    j = len(arr) - 1
    while i < j:
        while i < j and arr[i] < k:
            i += 1
        while i < j and arr[j] >= k:
            j -= 1
        if i < j:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
    if arr[i] < k:
        i += 1

    return (i, arr[:i], arr[i:])

def test(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    print 'partition: {}'.format(parttn(arr, k))

def main():
    '''partition'''
    arr = list(range(20))
    random.shuffle(arr)
    test(arr, 8)
    random.shuffle(arr)
    test(arr, 0)
    random.shuffle(arr)
    test(arr, 19)
    random.shuffle(arr)
    test(arr, -2)
    random.shuffle(arr)
    test(arr, 22)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
