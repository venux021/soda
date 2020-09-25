#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def get_sum(s):
    i = 0
    n = len(s)
    neg = False
    dbuf = []
    total = 0
    while i < n:
        if s[i] in '0123456789':
            dbuf.append(s[i])
        elif s[i] == '-':
            if dbuf:
                total += parse(neg, dbuf)
                dbuf.clear()
                neg = False
            neg = not neg
        else:
            if dbuf:
                total += parse(neg, dbuf)
                dbuf.clear()
            neg = False
        i += 1
    if dbuf:
        total += parse(neg, dbuf)
    return total

def parse(neg, dbuf):
    n = 0
    for d in dbuf:
        n = n * 10 + (ord(d) - 48)
    return -n if neg else n

@testwrapper
def test(s):
    print(s)
    print(get_sum(s))

def main():
    test('A1.3')
    test('A-1BC--12')
    test('A-1-2-.--3--4b50')

if __name__ == '__main__':
    main()
