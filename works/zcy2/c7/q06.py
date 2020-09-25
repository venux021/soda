#!/usr/bin/env python3
import math
import sys

from sodacomm.tools import testwrapper

def find_single(arr, k):
    a2 = [to_basek(i, k) for i in arr]
    print(a2)
    r = 0
    for n in a2:
        r = add_basek(r, n, k)
    return from_basek(r, k)

def getbit(k):
    return math.ceil(math.log2(k))

def to_basek(i, k):
    bit = getbit(k)
    if bit == 1:
        return i
    r = 0
    j = 0
    while i > 0:
        c = i % k
        r = r | (c << (bit*j))
        i = i // k
        j += 1
    return r

def add_basek(a, b, k):
    bit = getbit(k)
    mask = (1 << bit) - 1
    r = 0
    j = 0
    while a > 0 or b > 0:
        ax = a & mask
        bx = b & mask
        c = (ax + bx) % k
        r = r | (c << (bit*j))
        j += 1
        a >>= bit
        b >>= bit
    return r

def from_basek(n, k):
    bit = getbit(k)
    mask = (1 << bit) - 1
    i = 0
    r = 0
    while n > 0:
        r += (n & mask) * pow(k, i)
        n >>= bit
        i += 1
    return r

@testwrapper
def test(arr, k):
    print(arr, k)
    print(find_single(arr, k))

def main():
    test([1,1,1,5,6,6,6,9,9,9], 3)
    test([13,102,13,7,13,102,102,13,13,8,102,8,8,102,8,8], 5)
    test([13,102,13,0,13,102,102,13,13,8,102,8,8,102,8,8], 5)

if __name__ == '__main__':
    main()
