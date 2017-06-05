#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def sum_len(arr, k):
    m = {0: -1}
    L = 0
    sm = 0
    n = len(arr)

    for i in range(n):
        sm += arr[i]
        if sm-k in m:
            j = m[sm-k]
            L = max(i-j, L)
        if sm not in m:
            m[sm] = i
    return L

def pn_len(arr):
    a2 = []
    for i in arr:
        if i > 0:
            a2.append(1)
        elif i < 0:
            a2.append(-1)
        else:
            a2.append(0)
    return sum_len(a2, 0)

def z1_len(arr):
    a2 = [-1 if i == 0 else 1 for i in arr]
    return sum_len(a2, 0)

def test(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    print 'sum len: {}'.format(sum_len(arr, k))
    print '+-: {}'.format(pn_len(arr))
    print '01: {}'.format(z1_len(arr))

def main():
    '''未排序数组中累加和为给定值的最长子数组系列问题'''
    test([1,2,3,3], 6)
    test([-4,6,3,-5,0,2,9,0,0,-7,-10,3,-8,-5,8,2], 5)
    test([0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,1,1,0], 5)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
