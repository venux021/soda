#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def min_cut(s):
    n = len(s)
    p = [[False] * n for i in range(n)]

    dp = [0] * (n + 1)
    dp[-1] = -1

    for i in range(1, n):
        cut = i
        for j in range(i, -1, -1):
            if s[i] == s[j] and (i-j<2 or p[j+1][i-1]):
                p[j][i] = True
                cut = min(cut, dp[j-1] + 1)
        dp[i] = cut

    print dp

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
