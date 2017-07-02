#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def z_seq(m):
    row = len(m)
    if row == 0:
        return []
    col = len(m[0])
    if col == 0:
        return []

    if row == 1:
        return m[0][:]
    if col == 1:
        return map(lambda x: x[0], m)

    result = [m[0][0]]

    rt = [0, 1]
    Lb = [1, 0]
    direction = 0

    while rt != Lb:
        if direction == 0:
            i, j = rt
            while i <= Lb[0] and j >= Lb[1]:
                result.append(m[i][j])
                i += 1
                j -= 1
        else:
            i, j = Lb
            while i >= rt[0] and j <= rt[1]:
                result.append(m[i][j])
                i -= 1
                j += 1
        direction = 1 - direction

        if rt[1] < col - 1:
            rt[1] += 1
        else:
            rt[0] += 1
        if Lb[0] < row - 1:
            Lb[0] += 1
        else:
            Lb[1] += 1

    result.append(m[row-1][col-1])

    return result

def test(m):
    print 'm: {}'.format(m)
    print 'z: {}'.format(z_seq(m))
    print '----'

def main():
    '''之字形打印矩阵'''
    test([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    test([[1,2],[3,4],[5,6],[7,8]])
    test([[1,2,3,4,5],[6,7,8,9,10]])
    test([[5,6,7,8]])
    test([[1],[2],[3],[4]])
    test([[1]])
    test([])
    test([[]])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
