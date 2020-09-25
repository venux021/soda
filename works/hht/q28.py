#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def _pp(chars, i, j):
    if i == j:
        print(''.join(chars))
        return

    for k in range(i, j+1):
        t = chars[k]
        chars[k] = chars[i]
        chars[i] = t
        _pp(chars, i+1, j)
        t = chars[k]
        chars[k] = chars[i]
        chars[i] = t


def print_permutation(chars):
    _pp(chars, 0, len(chars)-1)

def test(s):
    print_permutation(list(s))

def test2(s, k):
    print('k:', k)
    print_combination(s, k)
    print('------')

def print_combination(s, k):
    buf = [0] * k
    _pc(s, 0, k, buf, 0) 

def _pc(src, p, k, buf, x):
    if x == len(buf):
        print(''.join(buf))
        return

    n = len(src) - p
    if k > n:
        return

    buf[x] = src[p]
    _pc(src, p+1, k-1, buf, x+1)

    _pc(src, p+1, k, buf, x)

def main():
    '''字符串的排列'''
#    test('abc')
#    test('x')
#    test('12345')
#    test('ui')
    test2('abc', 2)
    test2('1', 1)
    test2('xy', 1)
    test2('1234567', 4)
    test2('1234567', 6)
    test2('1234567', 1)
    test2('1234567', 7)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
