#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def acc_mult(arr):
    n = len(arr)
    r = [0] * n
    c = 1
    for i in range(n):
        c *= arr[i]
        r[i] = c

    c = 1
    for i in range(n-1, -1, -1):
        if i > 0:
            r[i] = r[i-1] * c
            c *= arr[i]
        else:
            r[i] = c

    return r

def test(arr):
    print 'arr: {}'.format(arr)
    print 'result: {}'.format(acc_mult(arr))

def main():
    '''不包含本位置值的累乘数组'''
    test([2,3,1,4])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
