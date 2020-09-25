#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

UP = 0
LEFT = 1
EQ = -1

def mcss(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * n for i in range(m)]
    path = [[0] * n for i in range(m)]

    for i in range(m):
        if s1[i] == s2[0]:
            dp[i][0] = 1
            path[i][0] = EQ
    for j in range(1, n):
        if s1[0] == s2[j]:
            dp[0][j] = 1
            path[0][j] = EQ

    for i in range(1, m):
        for j in range(1, n):
            k2 = dp[i-1][j]
            k3 = dp[i][j-1]
            if k2 > k3:
                dr = UP
                dp[i][j] = k2
            else:
                dr = LEFT
                dp[i][j] = k3
            if s1[i] == s2[j]:
                k1 = dp[i-1][j-1] + 1
                if k1 > dp[i][j]:
                    dr = EQ
                    dp[i][j] = k1
            path[i][j] = dr

    L = dp[m-1][n-1]
    seq = [' '] * L
    p = L
    i = m-1
    j = n-1
    while p > 0:
        if path[i][j] == UP:
            i -= 1
        elif path[i][j] == LEFT:
            j -= 1
        else:
            p -= 1
            seq[p] = s1[i]
            i -= 1
            j -= 1

    return ''.join(seq)

def test(s1, s2):
    print 's1: {}, s2: {}'.format(s1, s2)
    print 'max common sub seq: {}'.format(mcss(s1, s2))

def main():
    '''最长公共子序列问题'''
    test('1a2c3d4b56', 'b1d23ca45b6a')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
