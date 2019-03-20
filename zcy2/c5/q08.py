#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def all_chars_once(s):
    m = [0] * 128
    for c in s:
        k = ord(c)
        if m[k] == 0:
            m[k] = 1
        else:
            return False
    return True

@testwrapper
def test(s):
    print(s)
    print(all_chars_once(s))

def main():
    test('abc')
    test('121')

if __name__ == '__main__':
    main()
