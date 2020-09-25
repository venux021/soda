#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def minc(s):
    n = len(s)
    m = [[False] * n for i in range(n)]
    dp = [0] * (n + 1)
    dp[-1] = -1

    for i in range(n-2, -1, -1):
        dp[i] = 0x7fffffff
        for j in range(i, n):
            if s[i] == s[j] and (j-i<2 or m[i+1][j-1]):
                m[i][j] = True
                dp[i] = min(dp[i], dp[j+1] + 1)
    return dp[0]

def test(s):
    print 's: {}, n: {}'.format(s, minc(s))

def main():
    '''回文最少分割数'''
    test('A')
    test('ABA')
    test('ACDCDCDAD')
    test('AB')
    test('AAA')
    test('ABCD')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
