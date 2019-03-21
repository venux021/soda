#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def get_num(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    n1, n2 = 1, 2
    i = 2
    for i in range(2, n):
        k = n1 + n2
        n1 = n2
        n2 = k
    return k

@testwrapper
def test(n):
    print(n, get_num(n))

def main():
    test(1)
    test(5)
    test(8)
    test(10)

if __name__ == '__main__':
    main()
