#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def remove_0_ktimes(s, k):
    buf = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] != '0':
            buf.append(s[i])
            i += 1
        else:
            j = i
            while j < n and s[j] == '0':
                j += 1
            if j - i != k:
                for _ in range(j-i):
                    buf.append('0')
            i = j
    return ''.join(buf)

@testwrapper
def test(s, k):
    print(s, k)
    print(remove_0_ktimes(s, k))

def main():
    test('A00B', 2)
    test('A0000B000', 3)

if __name__ == '__main__':
    main()
