#!/usr/bin/env python3
import random
import sys

from sodacomm.tools import testwrapper

def randomx(k):
    a = random.random()
    for i in range(k-1):
        a = max(a, random.random())
    return a

@testwrapper
def test(k):
    print(randomx(k))

def main():
    test(1)
    test(2)
    test(5)
    test(10)

if __name__ == '__main__':
    main()
