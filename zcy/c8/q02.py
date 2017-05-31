#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def rotate(m):
    row = len(m)
    i = 0
    a = 0
    b = row - 1
    while a <= b:
        for j in range(a, b):
            t = m[i][j]
            m[i][j] = m[row-j-1][i]
            m[row-j-1][i] = m[row-i-1][row-j-1]
            m[row-i-1][row-j-1] = m[j][row-i-1]
            m[j][row-i-1] = t
        i += 1
        a += 1
        b -= 1

def print_matrix(m):
    for i in range(len(m)):
        L = []
        for j in range(len(m[i])):
            L.append(str(m[i][j]))
        print ','.join(L)

def test(m):
    print_matrix(m)
    rotate(m)
    print_matrix(m)
    print '----'

def main():
    '''将正方形矩阵顺时针转动90度'''
    test([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
    test([[1,2,3],[4,5,6],[7,8,9]])
    test([[1,2],[3,4]])
    test([[1]])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
