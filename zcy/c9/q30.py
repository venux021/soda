#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def max_len(s):
    n = len(s)
    mx = [[0] * n for i in range(n)]

    for i in range(n):
        mx[i][i] = 1

    mxl = 1
    a = b = 0
    for L in range(2, n+1):
        for i in range(0, n-L+1):
            j = i + L - 1
            if L == 2:
                if s[i] == s[j]:
                    mx[i][j] = 2
                    if mxl < 2:
                        mxl = 2
                        a,b = i,j
            else:
                if s[i] == s[j] and mx[i+1][j-1] > 0:
                    mx[i][j] = mx[i+1][j-1] + 2
                    if mx[i][j] > mxl:
                        mxl = mx[i][j]
                        a,b = i,j
    return s[a:b+1]

def append(s):
    pass


def test(s):
    print 's: {}'.format(s)
    print 'len: {}'.format(max_len(s))
    print 'append: {}'.format(append(s))

def main():
    '''Manacher算法'''
    test('123')
    test('1223')
    test('abc1234321ab')
    test('421abcba1234321ac')
    test('421abcba1234321ab')
    test('12345654321')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
