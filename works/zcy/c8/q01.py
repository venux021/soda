#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def cir_print(m):
    row = len(m)
    col = len(m[0])

    seq = []
    lr = lc = 0
    rr = row - 1
    rc = col - 1
    while lr < rr and lc < rc:
        R = lr
        C = lc
        while C < rc:
            seq.append(m[R][C])
            C += 1
        while R < rr:
            seq.append(m[R][C])
            R += 1
        while C > lc:
            seq.append(m[R][C])
            C -= 1
        while R > lr:
            seq.append(m[R][C])
            R -= 1
        lr += 1
        lc += 1
        rr -= 1
        rc -= 1
    if lr == rr:
        for i in range(rc-lc+1):
            seq.append(m[lr][lc+i])
    elif lc == rc:
        for i in range(rr-lr+1):
            seq.append(m[lr+i][lc])

    seq = [str(i) for i in seq]

    return seq

def test(m):
    print 'm: {}'.format(m)
    print 'cir: {}'.format(','.join(cir_print(m)))

def main():
    '''转圈打印矩阵'''
    test([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]])
    test([[1,2,3],[4,5,6],[7,8,9]])
    test([[1]])
    test([[1,2,3]])
    test([[1],[2],[3]])
    test([[1,2],[3,4]])
    test([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
    test([[1,2],[3,4],[5,6],[7,8]])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
