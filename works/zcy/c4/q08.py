#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def mcs(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * n for i in range(m)]

    for i in range(m):
        if s1[i] == s2[0]:
            dp[i][0] = 1
    for i in range(n):
        if s1[0] == s2[i]:
            dp[0][i] = 1
    L = 0
    for i in range(1, m):
        for j in range(1, n):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0
            L = max(L, dp[i][j])

    return L

def mcs2(s1, s2):
    m = len(s1)
    n = len(s2)

    L = 0

    for i in range(m):
        k = i
        j = 0
        _len = 0
        while k < m and j < n:
            if s1[k] == s2[j]:
                _len += 1
                L = max(L, _len)
            else:
                _len = 0
            j += 1
            k += 1
        if m - i < L:
            break

    for j in range(1, n):
        i = 0
        k = j
        _len = 0
        while k < n and i < m:
            if s1[i] == s2[k]:
                _len += 1
                L = max(L, _len)
            else:
                _len = 0
            i += 1
            k += 1
        if n - j < L:
            break

    return L

def test(s1, s2):
    print 's1: {}, s2: {}'.format(s1, s2)
    print 'max common sub: {}'.format(mcs(s1, s2))
    print 'max common sub 2: {}'.format(mcs2(s1, s2))

def main():
    '''最长公共子串问题'''
    test('1ab2345cd', '12345ef')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
