#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def max_mult(arr):
    n = len(arr)
    r_max = _min = _max = arr[0]
    for i in range(1, n):
        next_min = min(_min * arr[i], _max*arr[i], arr[i])
        _max = max(_min * arr[i], _max*arr[i], arr[i])
        _min = next_min
        r_max = max(_max, r_max)
    return r_max


def test(arr):
    print 'arr: {}'.format(arr)
    print 'max_mult: {}'.format(max_mult(arr))

def main():
    '''数组中子数组的最大累乘积'''
    test([-2.5, 4, 0, 3, 0.5, 8, -1])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
