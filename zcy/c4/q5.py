#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def coins(arr, aim):
    if aim <= 0:
        return 1

    row = len(arr)
    col = aim + 1
    dp = [0] * col

    for i in range(0, col, arr[0]):
        dp[i] = 1

    for i in range(1, row):
        for j in range(1, col):
            if j >= arr[i]:
                dp[j] += dp[j-arr[i]]

    return dp[col-1]

def test(arr, aim):
    print 'arr: {}'.format(arr)
    print 'aim: {}'.format(aim)
    print coins(arr, aim)

def main():
    '''换钱方法数'''
    test([5,10,25,1], 0)
    test([5,10,25,1], 15)
    test([3,5], 2)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
