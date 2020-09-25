#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def F(arr, i, j):
    if i < j:
        return max(arr[i] + S(arr, i+1, j), arr[j] + S(arr, i, j-1))
    else:
        return arr[i]

def S(arr, i, j):
    if i < j:
        return min(F(arr,i+1,j), F(arr,i,j-1))
    else:
        return 0

def win_score(arr):
    n = len(arr)
    return max(F(arr, 0, n-1), S(arr, 0, n-1))

def win_score_2(arr):
    n = len(arr)
    fm = [[0] * n for i in range(n)]
    sm = [[0] * n for i in range(n)]

    for i in range(n):
        fm[i][i] = arr[i]

    for L in range(2, n+1):
        i = 0
        j = L-1
        while j < n:
            fm[i][j] = max(arr[i]+sm[i+1][j], arr[j]+sm[i][j-1])
            sm[i][j] = min(fm[i+1][j], fm[i][j-1])
            i += 1
            j += 1

    return max(fm[0][n-1], sm[0][n-1])

def test(arr):
    print 'arr: {}'.format(arr)
    print 'winner score: {}'.format(win_score(arr))
    print 'winner score 2: {}'.format(win_score_2(arr))
    print '----'

def main():
    '''排成一条线的纸牌博弈问题'''
    test([1,2,100,4])
    test([1,100,2])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
