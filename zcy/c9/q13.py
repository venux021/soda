#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def get_stat(arr):
    n = len(arr)

    for i in range(n):
        if i < 0:
            continue
        elif arr[i] == i:
            cap = i
            continue
        j = i
        last = -1
        while arr[j] != j and arr[j] >= 0:
            k = j
            j = arr[j]
            arr[k] = last
            last = k

        L = 0 if arr[j] == j else -arr[j]
        j = last
        while j >= 0:
            L += 1
            k = j
            j = arr[j]
            arr[k] = -L

    arr[cap] = 0

    for i in range(n):
        if arr[i] >= 0:
            continue
        j = i
        k = j
        j = -arr[j]
        arr[k] = 0

        while arr[j] < 0:
            k = j
            j = -arr[j]
            arr[k] = 1
        arr[j] += 1

    arr[0] = 1

    return arr

def test(arr):
    print 'arr: {}'.format(arr)
    print 'stat: {}'.format(get_stat(arr))

def main():
    '''路径数组变为统计数组'''
    test([9,1,4,9,0,4,8,9,0,1])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
