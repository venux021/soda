#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def s(arr):
    if len(arr) == 1:
        return 0
    else:
        return min(f(arr[1:]), f(arr[:-1]))

def f(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0] + s(arr[1:]), arr[-1] + s(arr[:-1]))

def win(arr):
    return max(f(arr), s(arr))

def winx(arr):
    n = len(arr)
    fm = [[0] * n for i in range(n)]
    sm = [[0] * n for i in range(n)]
    for i in range(n):
        fm[i][i] = arr[i]

    for i in range(1,n):
        r = 0
        c = i
        while c < n:
            fm[r][c] = max(arr[c] + sm[r][c-1], arr[r] + sm[r+1][c])
            sm[r][c] = min(fm[r][c-1], fm[r+1][c])
            c += 1
            r += 1

    return max(fm[0][n-1], sm[0][n-1])

def test(arr):
    print 'arr: {}'.format(arr)
    print 'win: {}'.format(win(arr))
    print 'winx: {}'.format(winx(arr))

def main():
    '''纸牌博弈'''
    test([1,2,100,4])
    test([1,100,2])
    test([1,8,7,0,1,2,5,1,0,3,3])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
