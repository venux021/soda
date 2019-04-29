#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def count_1(n):
    if n == 0:
        print('haha')
        return 0
    if n < 10:
        return 1

    bits = get_bits(n)
    p = pow_of_10(bits-1)

    first_digit = n // p
    if first_digit == 1:
        a = n % p + 1
    else:
        a = p

    b = first_digit * (bits-1) * pow_of_10(bits-2)

    return a + b + count_1(n % p)

def pow_of_10(k):
    return int(pow(10, k))

def get_bits(n):
    i = 0
    while n > 0:
        i += 1
        n //= 10
    return i

@testwrapper
def test(n):
    print(n)
    print(count_1(n))

def main():
    test(21345)
    test(99)
    test(100)
    test(101)

if __name__ == '__main__':
    main()
