#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def replace_continuous(s, f, t):
    buf = []
    start = 0
    last_tail = -1
    while True:
        i = dofind(s, f, start)
        if i == -1:
            break
        if i > start:
            buf.append(s[start:i])
        if last_tail < i - 1:
            buf.append(t)
        start = i + len(f)
        last_tail = start - 1
    if start < len(s):
        buf.append(s[start:])
    return ''.join(buf)

def dofind(s, f, j):
    i = 0
    while i < len(f) and j < len(s):
        if f[i] == s[j]:
            i += 1
            j += 1
        else:
            i = 0
            j = j - i + 1
    return j - len(f) if i == len(f) else -1

@testwrapper
def test(s, f, t):
    print(s, f, t)
    print(replace_continuous(s, f, t))

def main():
    test('123abc', 'abc', '4567')
    test('123', 'abc', '456')
    test('123abcabc', 'abc', 'X')
    test('123abcabcabcxyz', 'abc', 'X')

if __name__ == '__main__':
    main()
