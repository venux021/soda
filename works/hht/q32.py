#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def count_digit_one(n, c):
    if c == 1:
        return 1

    first_digit = n // pow(10, c-1)
    remain = n % pow(10, c-1)
    if first_digit == 1:
        a = remain + 1
    else:
        a = pow(10, c-1)

    b = pow(10, c-2) * (c-1) * first_digit

    return a + b + count_digit_one(remain, c-1)

def count_1(n):
    c = 0
    k = n
    while k > 0:
        c += 1
        k = k // 10
    return count_digit_one(n, c)

def test(n):
    print('n: {}, count of 1: {}'.format(n, count_1(n)))

def main():
    '''从1到n整数中1出现的次数'''
    test(13467)
    test(21345)
    test(23)
    test(15)
    test(6)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
