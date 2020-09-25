#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def sym(s):
    n = len(s)
    dp = [[0]*n for i in range(n)]

    for L in range(1, n):
        for i in range(0, n-1):
            for j in range(i+L-1, n):
                if L == 1:
                    dp[i][j] = 0 if s[i] == s[j] else 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1

    Len = dp[0][n-1]
    result = [' '] * (Len + n)
    N = len(result)
    i = 0
    j = n-1
    p = 0
    while i <= j:
        if s[i] == s[j]:
            result[p] = result[N-1-p] = s[i]
            i += 1
            j -= 1
        elif dp[i+1][j] < dp[i][j-1]:
            result[p] = result[N-1-p] = s[i]
            i += 1
        else:
            result[p] = result[N-1-p] = s[j]
            j -= 1
        p += 1

    return ''.join(result)

def test(s):
    print 's: {}'.format(s)
    print 'x: {}'.format(sym(s))

def sym2(s1, s2):
    res_len = 2 * len(s1) - len(s2)
    result = [' '] * res_len

    i = 0
    j = len(s2) - 1
    p = 0
    left = 0
    right = len(s1) - 1
    while i <= j:
        L = left
        while s1[L] != s2[i]:
            L += 1
        R = right
        while s1[R] != s2[i]:
            R -= 1
        ks = list(s1[left:L] + s1[R+1:right+1][::-1])
        result[p:p+len(ks)] = ks

        ks = list(s1[R+1:right+1] + s1[left:L][::-1])
        result[len(result)-p-len(ks):len(result)-p] = ks

        left = L + 1
        right = R - 1
        p += len(ks)

        result[p] = result[len(result)-p-1] = s2[i]
        i += 1
        j -= 1
        p += 1

    return ''.join(result)

def test2(s1, s2):
    print 's1: {}, s2: {}'.format(s1, s2)
    print 'x: {}'.format(sym2(s1, s2))

def main():
    '''添加最少字符使字符串整体都是回文字符串'''
    test('A1B21C')
    test2('A1BC22DE1F', '1221')
    test2('Ak1BC22DE1dF', '1221')
    test2('Ak1BC2x2DE1dF', '12x21')
    test2('Ak1BC2xu1s2DE1dF', '12s21')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
