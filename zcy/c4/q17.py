#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def process(loc, i):
    n = len(loc)
    if i == n:
        return 1

    r = 0
    for k in range(n):
        for j in range(0, i):
            if loc[j] == k or abs(i-j) == abs(k-loc[j]):
                break
        else:
            loc[i] = k
            r += process(loc, i+1)
    return r

def proc2(upper, col, left_diag, right_diag):
    if upper == col:
        return 1

    r = 0
    pos = upper & ~(col | left_diag | right_diag)
    while pos != 0:
        i = pos & (~pos + 1)
        pos -= i
        r += proc2(upper, col | i, 
                ((left_diag | i) << 1) & 0xffffffff,
                ((right_diag | i) >> 1))
    return r


def queen2(n):
    return proc2(0xffffffff >> (32-n), 0, 0, 0)
            

def queen(n):
    return process([0] * n, 0)

def test(n):
    print 'n: {}, q: {}'.format(n, queen(n))

def test2(n):
    print 'n: {}, q2: {}'.format(n, queen2(n))


def main():
    '''N皇后问题'''
    for i in range(1, 12):
        test(i)
    for i in range(1, 15):
        test2(i)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
