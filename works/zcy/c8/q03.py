#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def zpath(m):
    row = len(m)
    col = len(m[0])
    ar = ac = br = bc = 0
    step = 1
    direct = 0
    result = []
    while step <= (row+col):
        if direct == 0:
            i = ar
            j = ac
            while i >= br and j <= bc:
                result.append(str(m[i][j]))
                i -= 1
                j += 1
        else:
            i = br
            j = bc
            while i <= ar and j >= ac:
                result.append(str(m[i][j]))
                i += 1
                j -= 1
        if ar < row - 1:
            ar += 1
        else:
            ac += 1
        if bc < col - 1:
            bc += 1
        else:
            br += 1
        direct = 1 - direct
        step += 1

    return ','.join(result)


def test(m):
    print 'm: {}'.format(m)
    print 'z: {}'.format(zpath(m))
    print '----'

def main():
    '''之字形打印矩阵'''
    test([[1]])
    test([[1,2,3,4,5]])
    test([[1],[2],[3]])
    test([[1,2],[3,4]])
    test([[1,2,3,4,5],[6,7,8,9,10]])
    test([[1,2],[3,4],[5,6],[7,8]])
    test([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
