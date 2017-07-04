#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def process(s, e, si, ei):
    sn = len(s)
    en = len(e)
    if ei == en:
        return si == sn
    elif ei + 1 == en or e[ei+1] != '*':
        return si != sn and (s[si] == e[ei] or e[ei] == '.') and process(s, e, si+1, ei+1)
    else:
        while si < sn and (s[si] == e[ei] or e[ei] == '.'):
            if process(s, e, si, ei + 2):
                return True
            si += 1
        return process(s, e, si, ei + 2)

def is_match_2(s, e):
    n = len(s)
    m = len(e)

    if m == 0:
        return n == 0
    elif n == 0:
        return m == 2 and e[-1] == '*'

    dp = [[False] * (m+1) for i in range(n+1)]

    dp[n][m] = True
    for i in range(m-2, -1, -2):
        if e[i+1] == '*':
            dp[n][i] = True
        else:
            break

    if e[-1] == '.' or e[-1] == s[-1]:
        dp[n-1][m-1] = True

    for i in range(n-1, -1, -1):
        for j in range(m-2, -1, -1):
            if e[j+1] != '*':
                dp[i][j] = (s[i] == e[j] or e[j] == '.') and dp[i+1][j+1]
            else:
                k = i
                while k < n and (s[k] == e[j] or e[j] == '.'):
                    if dp[k][j+2]:
                        break
                    k += 1
                dp[i][j] = dp[k][j+2]

    return dp[0][0]

def is_match(s, e):
    return process(s, e, 0, 0)

def test(s, e):
    print 's: {}, e: {}'.format(s, e)
    print 'match: {}'.format(is_match(s, e))
    print 'match 2: {}'.format(is_match_2(s, e))

def main():
    '''字符串匹配问题'''
    test('abc', 'abc')
    test('abc', 'a.c')
    test('abcd', '.*')
    test('', '')
    test('', '.*')
    test('', '..*')
    test('kffcmcaaafui', 'kffcmca*f*ui')
    test('kffcmcaaaui', 'kffcmca*f*ui')
    test('kffcmcui', 'kffcmca*f*ui')
    test('ereoi', 'er.oik*a*b*')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
