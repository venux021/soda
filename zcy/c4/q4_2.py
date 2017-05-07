#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

MAX = 0x7fffffff

def min_coins_1(arr, aim):
    if aim <= 0:
        return 0

    row = len(arr)
    col = aim + 1
    dp = [[0] * col for i in range(row)]

    for i in range(1, col):
        dp[0][i] = MAX
    dp[0][arr[0]] = 1

    for i in range(1, row):
        for j in range(1, col):
            a = dp[i-1][j]
            if j >= arr[i]:
                b = dp[i-1][j-arr[i]] + 1
                dp[i][j] = min(a, b)
            else:
                dp[i][j] = a

    r = dp[row-1][col-1]
    return r if r < MAX else -1

def min_coins_2(arr, aim):
    if aim <= 0:
        return 0

    col = aim + 1
    dp = [MAX] * col

    dp[0] = 0
    dp[arr[0]] = 1

    for i in range(1, len(arr)):
        for j in range(col - 1, 0, -1):
            if j >= arr[i]:
                b = dp[j-arr[i]] + 1
                dp[j] = min(dp[j], b)

    r = dp[col-1]
    return r if r < MAX else -1

def test(arr, aim):
    print 'arr: {}'.format(arr)
    print 'aim: {}'.format(aim)
    print min_coins_1(arr, aim)
    print min_coins_2(arr, aim)

def main():
    '''arr值可重复，仅代表一张钱的面值，求最少货币数'''
    test([5,2,3], 20)
    test([5,2,5,3], 10)
    test([5,2,5,3], 15)
    test([5,2,5,3], 0)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
