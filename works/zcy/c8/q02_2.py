#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def rotate(m):
    row = len(m)
    if row == 0:
        return []
    col = len(m[0])
    if col == 0:
        return [[]]

    if row != col:
        return [[]]
    elif row == 1:
        return m

    n = row - 1
    for i in range(0, row / 2): 
        for j in range(i, row-i-1):
            t = m[i][j]
            m[i][j] = m[n-j][i]
            m[n-j][i] = m[n-i][n-j]
            m[n-i][n-j] = m[j][n-i]
            m[j][n-i] = t

def print_matrix(m):
    for i in range(len(m)):
        L = []
        for j in range(len(m[i])):
            L.append('{:3}'.format(m[i][j]))
        print ''.join(L)

def test(m):
    print_matrix(m)
    rotate(m)
    print ''
    print_matrix(m)
    print '----'

def main():
    '''将正方形矩阵顺时针转动90度'''
    test([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
    test([[1,2,3],[4,5,6],[7,8,9]])
    test([[1,2],[3,4]])
    test([[1]])
    test([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
    pass

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
