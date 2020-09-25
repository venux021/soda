#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def exchange(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return (a, b)

@testwrapper
def test(a, b):
    print(a, b)
    a, b = exchange(a, b)
    print(a, b)

def main():
    test(1, 2)

if __name__ == '__main__':
    main()
