#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def min_cut(s):
    n = len(s)
    p = [[False] * n for i in range(n)]
    for i in range(n):
        p[i][i] = True

    for L in range(2, n+1):
        for i in range(0, n-L+1):
            j = i + L - 1
            if L == 2 and s[i] == s[j]:
                p[i][j] = True
            elif L > 2:
                if s[i] == s[j] and p[i+1][j-1]:
                    p[i][j] = True

    dp = [0] * n

    for i in range(1, n):
        if p[0][i]:
            continue
        cut = i
        for j in range(0, i):
            if p[j+1][i]:
                cut = min(cut, dp[j] + 1)
        dp[i] = cut

    return dp[n-1]

def test(s):
    print 's: {}'.format(s)
    print 'min cut: {}'.format(min_cut(s))

def main():
    '''回文最少分割数'''
    test('aba')
    test('acdcdcdad')
    test('AB')
    test('AAA')
    test('ABCD')
    test('112')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
