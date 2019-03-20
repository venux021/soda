#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def reverse_words(s):
    n = len(s)
    buf = [None] * n
    i = 0
    p = n - 1
    while i < n:
        if s[i] == ' ':
            buf[p] = ' '
            i += 1
            p -= 1
        else:
            j = i + 1
            while j < n and s[j] != ' ':
                j += 1
            for k in range(j-1, i-1, -1):
                buf[p] = s[k]
                p -= 1
            i = j
    return ''.join(buf)

@testwrapper
def test(s):
    print(s)
    print(reverse_words(s))

def main():
    test('dog loves pig')
    test("I'm a student.")

if __name__ == '__main__':
    main()
