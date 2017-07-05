#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def get_hp(m):
    row = len(m)
    col = len(m[0])

    dp = [[0] * col for i in range(row)]
    dp[row-1][col-1] = 1 - m[row-1][col-1]

    for i in range(col-2, -1, -1):
        dp[row-1][i] = max(1, dp[row-1][i+1] - m[row-1][i])
    for i in range(row-2, -1, -1):
        dp[i][col-1] = max(1, dp[i+1][col-1] - m[i][col-1])

    for i in range(row-2, -1, -1):
        for j in range(col-2, -1, -1):
            dp[i][j] = max(1, min(dp[i][j+1]-m[i][j], dp[i+1][j]-m[i][j]))

    return dp[0][0]

def test(m):
    print 'm: {}, hp: {}'.format(m, get_hp(m))

def main():
    '''龙与地下城游戏问题'''
    test([[-2,-3,3],[-5,-10,1],[0,30,-5]])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
