#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def josephus(n, k):
    t = 0
    for i in range(2, n+1):
        t = (t + k) % i
    return t + 1

@testwrapper
def test(n, k):
    print(f'{n} {k} {josephus(n, k)}')

def main():
    test(5, 3)
    test(8, 5)

if __name__ == '__main__':
    main()
