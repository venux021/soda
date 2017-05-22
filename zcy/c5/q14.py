#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def isvalid(s):
    a = b = 0
    for c in s:
        if c == '(':
            a += 1
        elif c == ')':
            b += 1
        else:
            return False
        if b > a:
            return False
    return (a == b)

def maxvlen(s):
    n = len(s)
    dp = [0] * n

    for i in range(1, n):
        if s[i] == ')' and s[i-dp[i-1]-1] == '(':
            dp[i] = dp[i-1] + 2
            if i-dp[i-1]-2 >= 0:
                dp[i] += dp[i-dp[i-1]-2]

    return max(dp)

def test(s):
    print 's: {}, valid: {}, vlen: {}'.format(s, isvalid(s), maxvlen(s))

def main():
    '''括号字符串的有效性和最长有效长度'''
    test('()')
    test('(()())')
    test('(())')
    test('())')
    test('()(')
    test('()a()')
    test('()(())')
    test('()(()()(')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
