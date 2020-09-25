#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def optimal(L, p, size):
    if size == 0:
        return 0
    opt = 0
    for i in range(len(L)):
        if size >= L[i]:
            opt = max(opt, p[i] + optimal(L, p, size - L[i]))
    return opt

def dp_optimal(L, p, size):
    n = len(L)
    dp = [0] * (size + 1)

    for s in range(1, size+1):
        for i in range(n):
            if s >= L[i]:
                dp[s] = max(dp[s], p[i] + dp[s-L[i]])

    return dp[size]

def test(L, p, size):
    if size < 24:
        print('L: {}, p: {}, size: {}, max1: {}'.format(L, p, size, optimal(L,p,size)))
    print('L: {}, p: {}, size: {}, max2: {}'.format(L, p, size, dp_optimal(L,p,size)))
    print('----')

def main():
    '''钢条切割'''
    test([1,2,3,4,5,6,7,8,9,10], [1,5,8,9,10,17,17,20,24,30], 4)
    test([1,2,3,4,5,6,7,8,9,10], [1,5,8,9,10,17,17,20,24,30], 17)
    test([1,2,3,4,5,6,7,8,9,10], [1,5,8,9,10,17,17,20,24,30], 22)
    test([1,2,3,4,5,6,7,8,9,10], [1,5,8,9,10,17,17,20,24,30], 76)
    test([1,2,3,4,5,6,7,8,9,10], [1,5,8,9,10,17,17,20,24,30], 143)
    test([1,2,3,4,5,6,7,8,9,10], [1,5,8,9,10,17,17,20,24,30], 1143)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
