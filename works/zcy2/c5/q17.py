#!/usr/bin/env python3
import functools
import sys

from sodacomm.tools import testwrapper

def max_concat(strs):
    strs = convert(strs)
    return ''.join(sorted(strs, key = functools.cmp_to_key(docomp)))

def docomp(s1, s2):
    A = s1 + s2
    B = s2 + s1
    if A > B:
        return 1
    elif A < B:
        return -1
    else:
        return 0

def convert(strs):
    return list(map(lambda x: x.upper(), strs))

@testwrapper
def test(strs):
    print(strs)
    print(max_concat(strs))

def main():
    test(['abc', 'de'])
    test(['b', 'ba'])

if __name__ == '__main__':
    main()
