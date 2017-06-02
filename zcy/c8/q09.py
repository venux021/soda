#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def find_dual(arr, k):
    i = 0
    j = len(arr) - 1
    r = []
    while i < j:
        if arr[i] + arr[j] < k:
            i += 1
        elif arr[i] + arr[j] > k:
            j -= 1
        else:
            if i == 0 or arr[i] != arr[i-1]:
                r.append((arr[i], arr[j]))
            i += 1
            j -= 1
    return r

def find_tuple(arr, k):
    n = len(arr)
    if n < 3:
        return []

    r = []
    for i in range(n-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        m = k - arr[i]
        a = i + 1
        b = n-1
        while a < b:
            p = arr[a] + arr[b]
            if p < m:
                a += 1
            elif p > m:
                b -= 1
            else:
                if a == i + 1 or arr[a] != arr[a-1]:
                    r.append((arr[i], arr[a], arr[b]))
                a += 1
                b -= 1
    return r

def test(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    print 'dual: {}'.format(find_dual(arr, k))
    print 'tuple: {}'.format(find_tuple(arr, k))
    print '----'

def main():
    '''不重复打印排序数组中相加和为给定值的所有二元组和三元组'''
    test([-8,-4,-3,0,1,2,4,5,8,9], 10)
    test([-8,-4,-3,0,1,1,1,1,2,2,2,2,4,5,8,8,8,8,8,9], 10)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
