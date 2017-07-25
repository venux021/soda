#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from collections import deque

def palin(s):
    n = len(s)
    dp = [[0] * n for i in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1

    for L in range(3, n+1):
        for i in range(0, n-L+1):
            j = i + L - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])

    r = [' '] * dp[0][n-1]
    i, j = 0, n-1
    p = len(r)-1
    while i < j:
        if s[i] == s[j]:
            r[p] = r[len(r)-p-1] = s[i]
            p -= 1
            i += 1
            j -= 1
        elif dp[i][j-1] > dp[i+1][j]:
            j -= 1
        else:
            i += 1

    if i == j:
        r[p] = s[i]

    return ''.join(r[::-1])

def test(s):
    r = palin(s)
    print('str: {}, palindrome sub seq: {}, length: {}'.format(s, r, len(r)))

def main():
    '''最长回文子序列'''
    test('character')
    test('1a369b4c+d-*e!d#c@~sbkanvb')
    test('civic')
    test('racecar')
    test('aibohphobia')
    test('aa')
    test('ab')
    test('abc')
    test('a')
    test('abcabc')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
