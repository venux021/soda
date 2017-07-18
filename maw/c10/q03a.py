#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def test(arr):
    print('arr: {}'.format(arr))
    print('min:', min_multiply(arr))

def min_multiply(arr):
    n = len(arr)
    C = [i[1] for i in arr]
    C.append(arr[0][0])
    dp = [[0] * n for i in range(n)]
    loc = [[-1] * n for i in range(n)]

    for L in range(2, n+1):
        for i in range(0, n-L+1):
            j = i + L - 1
            M = 0x7fffffff
            for k in range(i, j):
                x = dp[i][k] + dp[k+1][j] + C[i-1]*C[k]*C[j]
                if x < M:
                    M = x
                    loc[i][j] = k
            dp[i][j] = M

    show_order(0, n-1, loc)
    print()
    return dp[0][n-1]

def show_order(i, j, loc):
    if i == j:
        print(i, end = '')
        return

    print('(', end = '')
    k = loc[i][j]
    show_order(i, k, loc)
    show_order(k+1, j, loc)
    print(')', end = '')

def main():
    '''矩阵连乘最少乘法次数'''
    test([(50,10),(10,40),(40,30),(30,5)])
    test([(15,23),(23,39),(39,14),(14,27),(27,46),(46,9),(9,81)])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
