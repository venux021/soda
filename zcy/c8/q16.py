#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def max_sum(arr):
    n = len(arr)
    sm = max_sm = arr[0]
    for i in range(1,n):
        if sm >= 0:
            sm += arr[i]
        else:
            sm = arr[i]
        max_sm = max(sm, max_sm)
    return max_sm

def max_sum2(arr):
    n = len(arr)
    r_max = _max = arr[0]
    for i in range(1, n):
        nmax = _max + arr[i]
        _max = max(nmax, arr[i])
        r_max = max(_max, r_max)
    return r_max

def test(arr):
    print 'arr: {}'.format(arr)
    print 'max sum: {}'.format(max_sum(arr))
    print 'max sum2: {}'.format(max_sum2(arr))

def main():
    '''子数组的最大累加和问题'''
    test([1,-2,3,5,-2,6,-1])
    test([3,7,6,5,2,8])
    test([-3,-7,-6,-5,-2,-8])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
