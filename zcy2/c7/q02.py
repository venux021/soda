#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def sign(k):
    return flip((k >> 31) & 1)

def flip(k):
    return k ^ 1

def get_max(a, b):
    c = a - b
    sc = sign(c)
    s2 = sc ^ 1
    return a * sc + b * s2

def get_max2(a, b):
    c = a - b
    sa = sign(a)
    sb = sign(b)
    sc = sign(c)
    diff_sign = sa ^ sb
    same_sign = flip(diff_sign)
    ret_a = diff_sign * sa + same_sign * sc
    ret_b = flip(ret_a)
    return ret_a * a + ret_b * b

@testwrapper
def test(a, b):
    print(a, b)
    print(get_max(a, b), get_max2(a, b))

def main():
    test(1, 5)
    test(5, 1)
    test(10, -2)
    test(2, 0)
    test(-4, 0)

if __name__ == '__main__':
    main()
