#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def parse_int(s):
    if s[0] == '0':
        return 0
    elif s[0] == '-':
        if len(s) == 1 or s[1] == '0':
            return 0
        else:
            return -parse_positive(s[1:])
    else:
        return parse_positive(s)

def parse_positive(s):
    n = 0
    for c in s:
        if c not in '0123456789':
            return 0
        k = ord(c) - ord('0')
        n = n * 10 + k
        if n < -2147483648 or n > 2147483647:
            return 0
    return n

@testwrapper
def test(s):
    print(s)
    print(parse_int(s))

def main():
    test('123')
    test('023')
    test('A13')
    test('0')
    test('2147483647')
    test('2147483648')
    test('-123')
    test('-0123')

if __name__ == '__main__':
    main()
