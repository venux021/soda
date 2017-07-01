#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def accum(arr):
    n = len(arr)
    zero = 0
    for i in arr:
        if i == 0:
            zero += 1

    if zero > 1:
        return [0] * n

    if zero == 1:
        index = 0
        m = 1
        for i in range(n):
            if arr[i] == 0:
                index = i
            else:
                m *= arr[i]
        r = [0] * n
        r[index] = m
        return r

    total = reduce(lambda a, b: a * b, arr, 1)

    r = [1] * n
    for i in range(n):
        r[i] = total / arr[i]
    
    return r

def test(arr):
    print 'arr: {}'.format(arr)
    print 'acc: {}'.format(accum(arr))

def main():
    '''不包含本位置值的数组'''
    test([2,3,1,4])
    test([1,5,3,0,2,6])
    test([2,5,9,0,3,0,2,1])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
