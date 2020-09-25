#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def get_stat(arr):
    n = len(arr)

    last = -1
    for i in range(n):
        if arr[i] == i:
            cap = i
            continue
        elif arr[i] < 0:
            continue

        j = i
        last = -1
        while arr[j] != j and arr[j] >= 0:
            k = j
            j = arr[j]
            arr[k] = last
            last = k

        if arr[j] == j:
            s = 0
        else:
            s = -arr[j]

        j = last
        s += 1
        while j >= 0:
            k = j
            j = arr[j]
            arr[k] = -s
            s += 1

    arr[cap] = 0

    for i in range(n):
        if arr[i] >= 0:
            continue

        j = arr[i]
        arr[i] = 0
        while True:
            j = -j
            if arr[j] >= 0:
                arr[j] += 1
                break
            else:
                k = j
                j = arr[j]
                arr[k] = 1

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
