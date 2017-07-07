#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def feb(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    r = [1,1]
    a = b = 1
    for i in range(3, n+1):
        k = a + b
        r.append(k)
        a = b
        b = k

    return r

def test1(n):
    print 'n: {}'.format(n)
    print 'feb 1: {}'.format(feb(n))
    print 'feb 2: {}'.format(feb2(n))
    print('-----')

def feb2(n):
    if n == 1 or n == 2:
        return 1
    m = mx_mult([[1,0]], mx_pow([[1,1],[1,0]], n-1))
    return m[0][0]

def mx_pow(mx, n):
    row = len(mx)
    col = len(mx[0])
    unit = [[0] * row for i in range(row)]
    for i in range(row):
        unit[i][i] = 1

    tmp = mx
    r = unit
    while n > 0:
        if n & 1 == 1:
            r = mx_mult(r, tmp)
        tmp = mx_mult(tmp, tmp)
        n >>= 1
    return r


def mx_mult(m1, m2):
    row = len(m1)
    col = len(m2[0])
    M = len(m2)
    result = [[0] * col for i in range(row)]

    for i in range(row):
        for j in range(col):
            r = 0
            for k in range(M):
                r += (m1[i][k] * m2[k][j])
            result[i][j] = r
    return result

def main():
    '''斐波那契系列问题的递归和动态规划'''
    test1(1)
    test1(2)
    test1(3)
    test1(10)
    test1(20)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
