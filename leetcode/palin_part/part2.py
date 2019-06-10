#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def minCut(s):
    n = len(s)
    if n == 0:
        return 0

    isp = [[0] * n for i in range(n)]
    dp = [0x7fffffff] * (n+1)
    dp[n] = -1
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j-i < 2 or isp[i+1][j-1]):
                isp[i][j] = 1
                dp[i] = min(dp[i], dp[j+1] + 1)

    return dp[0]

@testwrapper
def test(s):
    print(s)
    print(minCut(s))

def main():
    test('aab')
    test('abbacab')
    test('aba')
    test('aabaca')
    test('a')
    test('fddsdfasdfsddsadsdfadsdfasdfasdfaasdfafsdfsdadfasdfasdfasdfaddfdasdf')
    test('vdsfsacxvsadfazzdfsdvzsddzcvddasdfdcvxfadxcvzdfsdzxvcxdfdx')

if __name__ == '__main__':
    main()
