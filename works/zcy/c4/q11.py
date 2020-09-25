#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def health(mx):
    row = len(mx)
    col = len(mx[0])
    dp = [[0] * col for i in range(row)]
    dp[row-1][col-1] = max(1, 1 - mx[row-1][col-1])

    for i in range(row-2, -1, -1):
        dp[i][col-1] = max(1, dp[i+1][col-1] - mx[i][col-1])

    for i in range(col-2, -1, -1):
        dp[row-1][i] = max(1, dp[row-1][i+1] - mx[row-1][i])

    for i in range(row-2, -1, -1):
        for j in range(col-2, -1, -1):
            k = min(dp[i+1][j], dp[i][j+1])
            dp[i][j] = max(1, k - mx[i][j])

    return dp[0][0]

def main():
    '''龙与地下城'''
    mx = [[-2,-3,3],[-5,-10,1],[0,30,-5]]
    print health(mx)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
