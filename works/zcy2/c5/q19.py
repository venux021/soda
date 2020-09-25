#!/usr/bin/env python3
import string
import sys

from sodacomm.tools import testwrapper

def find_char(s, k):
    n = len(s)
    i = 0
    last_char = None
    while i < n:
        if i > k:
            return last_char
        if s[i] in string.ascii_lowercase:
            last_char = s[i]
            i += 1
        else:
            last_char = s[i:i+2]
            i += 2
    if i > k:
        return last_char

def find_char2(s, k):
    i = k - 1
    while i >= 0 and s[i] in string.ascii_uppercase:
        i -= 1
    num = k - 1 - i
    if num % 2 == 1:
        return s[k-1:k+1]
    elif s[k] in string.ascii_uppercase:
        return s[k:k+2]
    else:
        return s[k]

@testwrapper
def test(s, k):
    print(s, k)
    print(find_char(s, k))
    print(find_char2(s, k))

def main():
    test('aaABCDEcBCg', 4)
    test('aaABCDEcBCg', 7)
    test('aaABCDEcBCg', 10)

if __name__ == '__main__':
    main()
