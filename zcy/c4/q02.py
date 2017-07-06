#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def test(m):
    print 'm: {}'.format(m)
    print 'shortest path len: {}'.format(sp_len(m))

def sp_len(m):
    row = len(m)
    col = len(m[0])
    dp = [0] * col
    dp[0] = m[0][0]

    for i in range(1,col):
        dp[i] = dp[i-1] + m[0][i]

    for i in range(1,row):
        dp[0] += m[i][0]
        for j in range(1,col):
            dp[j] = min(dp[j], dp[j-1]) + m[i][j]

    return dp[-1]

def main():
    '''矩阵的最小路径和'''
    test([[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
