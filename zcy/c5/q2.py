#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def isdigit(s):
    if s is None:
        return False
    return s >= '0' and s <= '9'

def getsum(s):
    n = 0
    Sum = 0
    neg = False
    
    for c in s:
        if isdigit(c):
            if not neg:
                n = n * 10 + ord(c) - 48
            else:
                n = n * 10 - ord(c) + 48
        elif c == '-':
            if n != 0:
                Sum += n
                n = 0
                neg = False
            neg = not neg
        else:
            if n != 0:
                Sum += n
                n = 0
                neg = False
            neg = False

    if n != 0:
        Sum += n

    return Sum
    

def test(s):
    print 's: {}'.format(s)
    print 'sum: {}'.format(getsum(s))

def main():
    '''字符串中数字子串的求和'''
    test('A1.3')
    test('A-1BC--12')
    test('A1CD2E33')
    test('A-1B--2C--D6E')
    test('A--10-89')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
