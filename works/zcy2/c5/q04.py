#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def is_rotate(s1, s2):
    if len(s1) != len(s2):
        return False
    s3 = s2 + s2
    i = j = 0
    while i < len(s1) and j < len(s3):
        if s1[i] == s3[j]:
            i += 1
            j += 1
        else:
            i = 0
            j = j - i + 1
    return i == len(s1)

@testwrapper
def test(s1, s2):
    print(s1, s2)
    print(is_rotate(s1, s2))

def main():
    test('cdab', 'abcd')
    test('1ab2', 'ab12')
    test('2ab1', 'ab12')
    test('1234', '1234')

if __name__ == '__main__':
    main()
