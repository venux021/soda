#!/usr/bin/env python3
import itertools
import sys

from sodacomm.tools import testwrapper

def initial_life(mx):
    R = len(mx)
    C = len(mx[0])
    dp = [[0] * C for _ in range(R)]
    dp[R-1][C-1] = max(1, -mx[R-1][C-1])
    for c in range(C-2, -1, -1):
        dp[R-1][c] = max(1, dp[R-1][c+1] - mx[R-1][c])
    for r in range(R-2, -1, -1):
        dp[r][C-1] = max(1, dp[r+1][R-1] - mx[r][C-1])
    for i, j in itertools.product(range(R-2,-1,-1), range(C-2,-1,-1)):
        dp[i][j] = max(1, min(dp[i+1][j] - mx[i][j], dp[i][j+1] - mx[i][j]))
    return dp[0][0]

@testwrapper
def test(mx):
    print(mx)
    print(f'min initial life: {initial_life(mx)}')

def main():
    test([[-2,-3,3],[-5,-10,1],[0,30,-5]])

if __name__ == '__main__':
    main()
