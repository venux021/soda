#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def num2str(chars, num):
    base = len(chars)

    bits = 0
    p = 1
    n = num
    while n >= p:
        n -= p
        p *= base
        bits += 1

    buf = [chars[0]] * bits
    b = bits - 1
    while n > 0:
        v = pow(base, b)
        buf[b] = chars[n // v]
        n %= v
        b -= 1

    return ''.join(reversed(buf))

def str2num(chars, s):
    c2i = {c:i+1 for i,c in enumerate(chars)}
    base = len(chars)
    weight = 1
    n = 0
    for c in reversed(s):
        n += weight * c2i[c]
        weight *= base
    return n

@testwrapper
def test1(chars, num):
    print(chars, num)
    s = num2str(chars, num)
    n = str2num(chars, s)
    print(s, n)

def main():
    test1('ABC', 72)
    test1('ABC', 39)
    test1('ABC', 40)
    test1('ABC', 41)
    test1('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 18278)
    test1('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 17278)
    test1('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 18279)
    test1('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 30128)

if __name__ == '__main__':
    main()
