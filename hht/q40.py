#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def one_time(arr):
    xor = 0
    for v in arr:
        xor ^= v

    mask = xor & (~(xor-1))

    y = 0
    for v in arr:
        if v & mask == 1:
            y ^= v

    a = y
    b = xor ^ y
    return (a, b)

def test(arr):
    print('only one time: {}'.format(one_time(arr)))

def main():
    '''数组中只出现一次的数字'''
    test([1,1,3,2,2,6,9,9])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
