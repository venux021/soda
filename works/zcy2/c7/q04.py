#!/usr/bin/env python3
import ctypes
import sys

from sodacomm.tools import testwrapper

def count_one(n):
    n = ctypes.c_uint(n).value
    c = 0
    while n != 0:
        if n & 1 == 1:
            c += 1
        n = n >> 1
    return c

def count_one2(n):
    n = ctypes.c_uint(n).value
    c = 0
    while n != 0:
        c += 1
        n &= (n-1)
    return c

def count_one3(n):
    n = ctypes.c_uint(n).value
    c = 0
    while n != 0:
        c += 1
        n -= n & (~n + 1)
    return c

def count_one4(n):
    n = ctypes.c_uint(n).value
    n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
    n = (n & 0x0f0f0f0f) + ((n >> 4) & 0x0f0f0f0f)
    n = (n & 0x00ff00ff) + ((n >> 8) & 0x00ff00ff)
    n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff)
    return n

def mit_hackmem(n):
    n = ctypes.c_uint(n).value
    tmp = n - ((n >> 1) & 0o33333333333) - ((n >> 2) & 0o11111111111)
    tmp = (tmp + (tmp >> 3)) & 0o30707070707
    return tmp % 63

@testwrapper
def test(n):
    print(n)
    print(count_one(n), count_one2(n), count_one3(n), count_one4(n), mit_hackmem(n))

def main():
    test(0)
    test(5)
    test(21)
    test(27)
    test(-10)

if __name__ == '__main__':
    main()
