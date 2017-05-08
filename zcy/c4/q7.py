#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def Lcs(a, b):
    m = len(a)
    n = len(b)
    dp = [[0] * n for i in range(m)]

    p = 0
    for i in range(m):
        if p == 0 and b[0] == a[i]:
            p = 1
            dp[i][0] = 1
        elif p == 1:
            dp[i][0] = 1

    p = 0
    for i in range(n):
        if p == 0 and a[0] == b[i]:
            p = 1
            dp[0][i] = 1
        elif p == 1:
            dp[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            k = max(dp[i-1][j], dp[i][j-1])
            if a[i] == b[j]:
                k = max(k, dp[i-1][j-1] + 1)
            dp[i][j] = k

    cs = dp[m-1][n-1]
    r = []
    i = m-1
    j = n-1
    while cs > 0:
        if i > 0 and dp[i][j] == dp[i-1][j]:
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            r.append(a[i])
            i -= 1
            j -= 1
            cs -= 1
    
    r.reverse()
    return ''.join(r)


def test(a, b):
    print 'a:', a
    print 'b:', b
    print 'lcs:', Lcs(a, b)

def main():
    '''最长公共子序列'''
    test('1A2C3D4B56', 'B1D23CA45B6A')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
