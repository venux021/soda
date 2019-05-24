#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def count_digit_1(n):
    if n == 0:
        return 0
    if n < 10:
        return 1

    bits = get_bits(n)
    p10 = pow_of_10(bits-1)
    leading_digit = n // p10
    leading_1_count = p10 if leading_digit != 1 else (n % p10 + 1)

    remaining_1_count = leading_digit * (bits-1) * p10//10

    return leading_1_count + remaining_1_count + count_digit_1(n % p10)

def pow_of_10(n):
    r = 1
    for i in range(n):
        r *= 10
    return r

def get_bits(n):
    c = 0
    while n > 0:
        c += 1
        n //= 10
    return c

@testwrapper
def test(n):
    print(n)
    print(f'number of 1 from 1 to {n}: {count_digit_1(n)}')

def main():
    test(21345)
    test(99)
    test(100)
    test(101)

if __name__ == '__main__':
    main()
