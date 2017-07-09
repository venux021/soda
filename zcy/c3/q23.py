#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def total_bi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        k = 2 * dp[i-1]
        for j in range(1, i-1):
            k += (dp[j] * dp[i-1-j])
        dp[i] = k

    return dp[n]

def all_head(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]

    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        k = 2 * dp[i-1]
        for j in range(1, i-1):
            k += (dp[j] * dp[i-1-j])
        dp[i] = k

    r = []
    for i in range(1, n+1):
        r += ([i] * dp[i-1] * dp[n-i])
    return r

def test(n):
    print('n: {}, total: {}'.format(n, total_bi(n)))
    print('all head: {}'.format(all_head(n)))

def main():
    '''统计和生成所有不同的二叉树'''
    test(1)
    test(2)
    test(3)
    test(4)
    test(5)
#    test(8)
#    test(20)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
