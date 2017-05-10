#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def num1(d):
    if len(d) <= 1:
        return 1

    if d[0] == '0':
        return 0

    a = num1(d[1:])

    i = int(d[0:2])
    if i >= 10 and i <= 26:
        return a + num1(d[2:])
    else:
        return a

def num2(d):
    n = len(d)
    if n <= 1:
        return 1
    arr = [0] * n

    if d[n-1] != '0':
        arr[n-1] = 1
    else:
        arr[n-1] = 0

    if d[n-2] != '0':
        k = int(d[n-2:])
        if k >= 10 and k <= 26:
            arr[n-2] = 2
        else:
            arr[n-2] = 1
    else:
        arr[n-2] = 0

    for i in range(n-3, -1, -1):
        if d[i] == '0':
            arr[i] = 0
            continue

        k = int(d[i:i+2])
        if k >= 10 and k <= 26:
            arr[i] = arr[i+1] + arr[i+2]
        else:
            arr[i] = arr[i+1]

    return arr[0]

def test(d):
    print 'd: {}'.format(d)
    print 'num1: {}'.format(num1(d))
    print 'num2: {}'.format(num2(d))

def main():
    '''数字串转化为字母串的可能数量'''
    test('1111')
    test('01')
    test('10')
    test('1111111111')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
