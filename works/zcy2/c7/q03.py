#!/usr/bin/env python3
import sys
import time

from numpy import int32

from sodacomm.tools import testwrapper

def bit_add(a, b):
    while True:
        x = a ^ b
        b = (a & b) << 1
        if b == 0:
            return x
        a = x

def bit_minus(a, b):
    return bit_add(a, get_neg(b))

def get_neg(n):
    return bit_add(~n, 1)

def bit_multiply(a, b):
    if a == 0 or b == 0:
        return 0
    elif a < 0 and b < 0 or a > 0 and b > 0:
        r = 1
    else:
        r = -1
    if a < 0:
        a = get_neg(a)
    if b < 0:
        b = get_neg(b)

    t = 0
    while b > 0:
        if b & 1 == 1:
            t = bit_add(t, a)
        b = b >> 1
        a = a << 1
    
    if r == -1:
        return get_neg(t)
    else:
        return t

def bit_div(a, b):
    x = a if a >= 0 else get_neg(a)
    y = b if b >= 0 else get_neg(b)
    i = 31
    result = 0
    while i >= 0:
        p = y << i
        if x >= p:
            result = result | (1 << i)
            x = bit_minus(x, p)
        i = bit_minus(i, int32(1))
    if a >= 0 and b >= 0 or a <= 0 and b <= 0:
        return result
    else:
        return get_neg(result)

@testwrapper
def test(a, b):
    a = int32(a)
    b = int32(b)

    r1 = a + b
    r1_a = bit_add(a, b)
    if r1_a == r1:
        print(f'{a} + {b} = {r1}')
    else:
        print(f'bit_add error: {r1_a}')

    r2 = a - b
    r2_a = bit_minus(a, b)
    if r2_a == r2:
        print(f'{a} - {b} = {r2}')
    else:
        print('bit_minus error')

    r3 = a * b
    r3_a = bit_multiply(a, b)
    if r3_a == r3:
        print(f'{a} * {b} = {r3}')
    else:
        print('bit_multiply error')

    r4 = abs(a) // abs(b)
    r4_a = bit_div(a, b)
    if abs(r4_a) == abs(r4):
        print(f'{a} / {b} = {r4_a}')
    else:
        print(f'bit_div error: {r4_a}')

def main():
    test(45, -9)
    test(45, -7)

if __name__ == '__main__':
    main()
