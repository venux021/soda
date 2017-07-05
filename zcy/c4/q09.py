#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def min_cost(s1, s2, ic, dc, rc):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n+1) for i in range(m+1)]

    for i in range(1, m+1):
        dp[i][0] = dc * i
    for i in range(1, n+1):
        dp[0][i] = ic * i

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + rc
            k1 = dp[i-1][j] + dc
            k2 = dp[i][j-1] + ic
            dp[i][j] = min(k1, k2, dp[i][j])

    return dp[m][n]

def test(s1, s2, ic, dc, rc):
    print 's1: {}, s2: {}, ic: {}, dc: {}, rc: {}'.format(s1, s2, ic, dc, rc)
    print 'min cost: {}'.format(min_cost(s1, s2, ic, dc ,rc))
    print '-----'

def main():
    '''最小编辑代价'''
    test('abc', 'adc', 5, 3, 2)
    test('abc', 'adc', 5, 3, 100)
    test('abc', 'abc', 5, 3, 2)
    test('ab12cd3', 'abcdf', 5, 3, 2)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
