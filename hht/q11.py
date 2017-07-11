#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def magic_pow(a, n):
    if a == 0 and n < 0:
        return None

    isneg = n < 0
    if isneg:
        n = -n

    k = a
    r = 1
    while n:
        if n & 1 == 1:
            r *= k
        k *= k
        n >>= 1

    return r if not isneg else 1/float(r)

def test(a, n):
    print('pow({},{}) = {}'.format(a,n, magic_pow(a, n)))

def main():
    '''数值的整数次方'''
    test(1, 9)
    test(2, 8)
    test(3, 3)
    test(12, 1)
    test(5, 7)
    test(7, 12)
    test(9, 27)
    test(3, 0)
    test(4, -2)
    test(8, -9)
    test(0, -1)
    test(0, 0)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
