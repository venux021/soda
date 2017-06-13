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

def test(arr):
    print 'arr: {}'.format(arr)
    print 'max sum: {}'.format(max_sum(arr))

def main():
    '''子数组的最大累加和问题'''
    test([1,-2,3,5,-2,6,-1])
    test([3,7,6,5,2,8])
    test([-3,-7,-6,-5,-2,-8])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
