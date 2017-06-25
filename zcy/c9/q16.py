#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def count_1(n):
    if n < 10:
        return 1

    high, bit = analysis(n)

    remain = n - high * pow(10, bit-1)
    if high == 1:
        a = remain + 1
    else:
        a = pow(10, bit-1)

    b = high * (bit-1) * pow(10, bit-2)

    return a + b + count_1(remain)

def analysis(n):
    bit = 1
    while n > 10:
        n /= 10
        bit += 1
    return (n, bit)

def test(n):
    print 'n: {}'.format(n)
    print 'num of 1: {}'.format(count_1(n))

def main():
    '''1到n中1出现的次数'''
    test(114)
    test(21345)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
