#!/usr/bin/env python3
import itertools
import sys

from sodacomm.tools import testwrapper

def minimum_edit_cost(s1, s2, ic, dc, rc):
    R = len(s1)
    C = len(s2)
    dp = [[0] * (C+1) for _ in range(R+1)]
    for i in range(R+1):
        dp[0][i] = ic * i
    for i in range(C+1):
        dp[i][0] = dc * i
    for i, j in itertools.product(range(1,C+1), range(1,R+1)):
        dp[i][j] = min(dp[i-1][j] + dc, dp[i][j-1] + ic)
        if s1[i-1] == s2[j-1]:
            dp[i][j] = min(dp[i][j], dp[i-1][j-1])
        else:
            dp[i][j] = min(dp[i][j], dp[i-1][j-1] + rc)
    return dp[R][C]

@testwrapper
def test(s1, s2, ic, dc, rc):
    print(s1, s2, ic, dc, rc)
    print(minimum_edit_cost(s1, s2, ic, dc, rc))

def main():
    test('abc', 'adc', 5, 3, 2)
    test('abc', 'adc', 5, 3, 100)
    test('abc', 'abc', 5, 3, 2)

if __name__ == '__main__':
    main()
