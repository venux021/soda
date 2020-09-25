#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def num2char(chars, num):
    base = len(chars)
    n = 0
    m = num
    k = 1
    while m >= k:
        n += 1
        m -= k
        k *= base

    arr = [1] * n

    k /= base

    while n > 0:
        arr[len(arr)-n] += m / k
        m = m % k
        n -= 1
        k /= base

    return ''.join([chars[i-1] for i in arr])

def char2num(chars, ch):
    base = len(chars)
    r = []
    k = 1
    num = 0
    for i in range(len(ch)):
        c = ch[len(ch) - i - 1]
        j = chars.find(c)
        num += (j+1) * k
        k *= base
    return num

def convert(chars, s):
    if isinstance(s, str):
        return char2num(chars, s)
    else:
        return num2char(chars, s)

def test(chars, num):
    print 'chars: {}, num: {}'.format(chars, num)
    print 'conv: {}'.format(convert(chars, num))

def main():
    '''一种字符和数字的对应关系'''
    test('ABC', 72)
    test('ABC', 'BABC')
    test('ABC', 'CCC')
    test('ABC', 40)
    test('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ZZY')
    test('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 18281)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
