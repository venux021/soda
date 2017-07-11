#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def max_sub_mx_size(m):
    row = len(m)
    col = len(m[0])

    line = [0] * col

    area = 0
    for i in range(row):
        for j in range(col):
            if m[i][j] == 1:
                line[j] += 1
            else:
                line[j] = 0
        area = max(area, get_area(line))

    return area

def get_area(line):
    stk = []
    area = 0
    line.append(-1)
    for i in range(len(line)):
        while stk and line[stk[-1]] >= line[i]:
            j = stk.pop()
            if stk:
                left = stk[-1] + 1
            else:
                left = 0
            right = i - 1
            length = right - left + 1
            area = max(area, line[j] * length)
        stk.append(i)

    line.pop()
    return area

def test(m):
    print('max sub matrix: {}'.format(max_sub_mx_size(m)))

def main():
    '''求最大子矩阵的大小'''
    test([[0,0,0,0],[0,0,0,0]])
    test([[1,0,0,0],[0,0,0,0]])
    test([[0,0,0,0],[0,1,0,0]])
    test([[0,0,0,0],[0,0,0,1]])
    test([[1,1,1,1],[1,1,1,1]])
    test([[1,1,1,0]])
    test([[1,0,1,1],[1,1,1,1],[1,1,1,0]])
    test([
            [0,1,0,1,1,0],
            [1,0,1,0,1,1],
            [0,1,1,1,0,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1]])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
