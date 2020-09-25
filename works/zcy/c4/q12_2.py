#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time

def compose(s, i):
    if i == len(s):
        return 1
    elif s[i] == '0':
        return 0

    if i < len(s) - 1 and s[i+1] == '0':
        if s[i] > '2':
            return 0
        else:
            return compose(s, i+2)

    if i < len(s) - 1 and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6'):
        return compose(s, i+1) + compose(s, i+2)
    else:
        return compose(s, i+1)

def count(s):
    if s[0] == '0':
        return 0
    return compose(s, 0)

def count2(s):
    n = len(s)
    dp = [0] * (n+1)

    dp[-1] = 1
    for i in range(n-1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        elif i < n-1 and s[i+1] == '0':
            dp[i] = 0 if s[i] > '2' else dp[i+2]
        elif i < n-1 and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6'):
            dp[i] = dp[i+1] + dp[i+2]
        else:
            dp[i] = dp[i+1]

    return dp[0]

def test(s):
    a = time.time()
    v = count(s)
    b = time.time()
    e = (b-a) * 1000
    print '[1] s: {}, c: {}, e: {}'.format(s, v, e)

    a = time.time()
    v = count2(s)
    b = time.time()
    e = (b-a) * 1000
    print '[2] s: {}, c: {}, e: {}'.format(s, v, e)
    print '----'

def main():
    '''数字字符串转换为字母组合的种数'''
    test('1111')
    test('01')
    test('10')
    test('110')
    test('12209')
    test('122019')
    test('12409')
    test('15231763265146')
    test('215271471257')
    test('152317615219826163265146')
    test('2152714716254712651271257')
    test('122112111212112212112112112122121')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
