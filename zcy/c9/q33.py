#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def min_time_1(arr, k):
    n = len(arr)
    if n == 0:
        return 0
    elif k == 1:
        return sum(arr)
    elif k >= n:
        return max(arr)

    tm = 0x7fffffff
    for i in range(n):
        tm = min(tm, max(min_time_1(arr[:i], 1), min_time_1(arr[i:], k-1)))

    return tm

def min_time_2(arr, k):
    if k == 1:
        return sum(arr)

    n = len(arr)

    dp = [[0] * n for i in range(k+1)]

    s = 0
    for i in range(n-1):
        s += arr[i]
        dp[1][i] = s

    for i in range(2, k+1):
        dp[i][0] = arr[0]
        for j in range(1, n):
            s = 0
            M = 0x7fffffff
            for q in range(j, -1, -1):
                s += arr[q]
                M = min(M, max(s, dp[i-1][q-1]))
            dp[i][j] = M

    return dp[k][n-1]

def min_time_3(arr, k):
    if k == 1:
        return sum(arr)

    n = len(arr)

    dp = [[0] * n for i in range(k+1)]

    s = 0
    for i in range(n-1):
        s += arr[i]
        dp[1][i] = s

    sm = arr[0]
    for i in range(2, k+1):
        dp[i][i-1] = max(arr[i-1], sm)
        for j in range(i, n):
            s = 0
            M = 0x7fffffff
            for q in range(j, i-1, -1):
                s += arr[q]
                M = min(M, max(s, dp[i-1][q-1]))
            dp[i][j] = M

    return dp[k][n-1]

def test(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    print 'time 1: {}'.format(min_time_1(arr, k))
    print 'time 2: {}'.format(min_time_2(arr, k))
    print 'time 3: {}'.format(min_time_3(arr, k))

def main():
    '''画匠问题'''
    test([3,1,4], 2)
    test([1,1,1,4,3], 3)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
