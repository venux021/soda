#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

MAX = 0x7fffffff

def isdigit(c):
    return c >= '0' and c <= '9'

def conv(s):
    n = 0
    if len(s) > 10 or len(s) == 0:
        return 0
    elif len(s) > 1 and s[0] == '0':
        return 0
    r = 0
    i = 0
    neg = False
    if s[0] == '-':
        i = 1
        neg = True
    for c in s[i:]:
        if not isdigit(c):
            return 0
        else:
            r = r * 10 + ord(c) - 48
            if r > MAX:
                return 0
    if neg:
        return -1 * r
    else:
        return r

def test(s):
    print 's: {}'.format(s)
    print 'r: {}'.format(conv(s))

def main():
    '''将整数字符串转成整数值'''
    test('123')
    test('023')
    test('A13')
    test('0')
    test('2147483647')
    test('2147483648')
    test('-123')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
