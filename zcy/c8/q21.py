#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def max_sq(m):
    row = len(m)
    col = len(m[0])
    right = [[0] * col for i in range(row)]
    down = [[0] * col for i in range(row)]

    for i in range(row):
        s = 0
        for j in range(col-1, -1, -1):
            if m[i][j] == 1:
                s += 1
            else:
                s = 0
            right[i][j] = s

    for j in range(col):
        s = 0
        for i in range(row-1, -1, -1):
            if m[i][j] == 1:
                s += 1
            else:
                s = 0
            down[i][j] = s

    max_edge = 0
    for i in range(row):
        for j in range(col):
            for k in range(1, min(row-i+1, col-j+1) + 1):
                if (right[i][j] >= k and 
                        down[i][j] >= k and 
                        down[i][j + k - 1] >= k and 
                        right[i+k-1][j] >= k):
                    max_edge = max(max_edge, k)
    return max_edge

def test(m):
    print 'm: {}'.format(m)
    print 'max square: {}'.format(max_sq(m))

def main():
    '''边界都是1的最大正方形大小'''
    test([
            [0,1,1,1,1],
            [0,1,0,0,1],
            [0,1,0,0,1],
            [0,1,1,1,1],
            [0,1,0,1,1]
    ])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
