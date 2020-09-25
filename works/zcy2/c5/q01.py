#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def is_deformation(s1, s2):
    m = {}
    for c in s1:
        m[c] = m.get(c, 0) + 1
    for c in s2:
        if c not in m or m[c] == 0:
            return False
        m[c] -= 1
    return not any(m.values())

@testwrapper
def test(s1, s2):
    print(s1, s2)
    print(is_deformation(s1, s2))

def main():
    test('123', '231')
    test('123', '2331')

if __name__ == '__main__':
    main()
