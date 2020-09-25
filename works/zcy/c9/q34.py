#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def min_dist(arr, k):
    n = len(arr)
    w = [[0] * n for i in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            w[i][j] = w[i][j-1] + arr[j] - arr[(i+j)/2]

    dp = [[0] * n for i in range(k)]

    for i in range(n):
        dp[0][i] = w[0][i]

    points = [[0] * n for i in range(k)]
    for i in range(1, k):
        for j in range(i+1, n):
            m = 0x7fffffff
            for q in range(j, i-2, -1):
                x = dp[i-1][q-1] + w[q][j]
                if x < m:
                    m = x
                    points[i][j] = q
            dp[i][j] = m

    p = n-1
    index_list = [0] * k
    for i in range(k-1, -1, -1):
        pnext = points[i][p]
        index = (p + pnext)/2
        index_list[i] = index
        p = pnext - 1

    return (dp[k-1][n-1], index_list)

def test(arr, n):
    print 'arr: {}, n: {}'.format(arr, n)
    print 'min dist: {}'.format(min_dist(arr, n))

def main():
    '''邮局选址问题'''
    test([1,2,3,4,5,1000], 2)
    test([-3,-2,-1,0,1,2], 3)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
