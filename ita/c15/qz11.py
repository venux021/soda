#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

MAX = sys.maxsize
man_cost = 6
M = 100

def h(j):
    return 0.45 * j * j

def show_stoke(arr):
    n = len(arr)
    D = sum(arr)

    dp = [[0] * (D+1) for i in range(n)]

    for i in range(D+1):
        dp[0][i] = h(i)

    total = D
    for i in range(1, n):
        total -= arr[i-1]
        for j in range(0, total+1):
            dp[i][j] = MAX
            limit = min(total, j + arr[i])
            for k in range(0, limit+1):
                t = dp[i-1][k] + h(j)
                if arr[i] + j - k > M:
                    t += man_cost * (arr[i] + j - k - M)
                dp[i][j] = min(dp[i][j], t)
    print(dp[n-1][0])

def test(arr):
    show_stoke(arr)

def main():
    '''库存规划'''
    test([105,93,115,123,87,109])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
