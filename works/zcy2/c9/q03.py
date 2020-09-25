#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def one_location(n):
    if n <= 0:
        return -1
    res = 0
    while n > 0:
        n >>= 1
        res += n
    return res

@testwrapper
def test3(n):
    print(n)
    print(one_location(n))

def zero_num(n):
    if n < 0:
        return 0
    res = 0
    for i in range(5, n+1, 5):
        cur = i
        while cur % 5 == 0:
            res += 1
            cur //= 5
    return res

def zero_num2(n):
    if n < 0:
        return 0
    res = 0
    while n > 0:
        res += n // 5
        n //= 5
    return res

@testwrapper
def test(n):
    print(n)
    print(zero_num(n))
    print(zero_num2(n))

@testwrapper
def test2(n):
    print(n)
    print(zero_num2(n))

def main():
    test(3)
    test(5)
    test(1000)
    test(100000)
    test2(1000000000)
    test2(10000000000)
    test3(1)
    test3(2)
    test3(1000000000)

if __name__ == '__main__':
    main()
