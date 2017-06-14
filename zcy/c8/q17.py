#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def max_sum(m):
    row = len(m)
    col = len(m[0])
    top_max = 0 - 0x7fffffff
    for i in range(row):
        s = [0] * col
        for j in range(i, row):
            for k in range(col):
                s[k] += m[j][k]
            cur_sum = 0
            mx_sum = 0 - 0x7fffffff
            for k in range(col):
                cur_sum += s[k]
                mx_sum = max(mx_sum, cur_sum)
                cur_sum = cur_sum if cur_sum > 0 else 0
            top_max = max(top_max, mx_sum)
    return top_max

def test(m):
    print 'matrix: {}'.format(m)
    print 'max_sum: {}'.format(max_sum(m))

def main():
    '''子矩阵的最大累加和问题'''
    test([[-90,48,78],[64,-40,64],[-81,-7,66]])
    test([[-1,-1,-1],[-1,2,2],[-1,-1,-1]])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
