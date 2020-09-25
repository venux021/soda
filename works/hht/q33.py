#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import functools

def to_str(i):
    buf = []
    while i > 0:
        buf.append(ascii(i % 10))
        i = i // 10
    return ''.join(buf[::-1])

def to_min(arr):
    b = []
    for v in arr:
        b.append(to_str(v))

    b.sort(key = functools.cmp_to_key(mycmp))
    for i in range(len(b)):
        b[i] = int(b[i])

    return b

def mycmp(x, y):
    a = x + y
    b = y + x
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def test(arr):
    print('arr: {}'.format(arr))
    print('min: {}'.format(to_min(arr)))

def main():
    '''把数组排成最小的数'''
    test([3, 32, 321])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
