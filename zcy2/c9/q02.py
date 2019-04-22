#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def gcd(m, n):
    return gcd(n, m%n) if n != 0 else m

@testwrapper
def test(m, n):
    print(m, n)
    print(gcd(m, n))

def main():
    test(12, 8)
    test(7, 5)
    test(10, 1)
    test(36, 24)

if __name__ == '__main__':
    main()
