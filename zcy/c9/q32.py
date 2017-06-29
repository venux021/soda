#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time

def drop_chess(n, k, mx):
    if mx[n][k] > -1:
        return mx[n][k]

    if n == 0 or k == 0:
        mx[n][k] = 0
        return 0
    elif k == 1:
        mx[n][k] = n
        return n

    min_step = 0x7fffffff
    for i in range(1, n+1):
        m = max(drop_chess(i-1, k-1, mx), drop_chess(n-i, k, mx))
        min_step = min(min_step, m)

    mx[n][k] = min_step + 1
    return min_step + 1

def test(n, k):
    print 'n: {}, k: {}'.format(n, k)
    if n <= 500:
        mx = [[-1] * (k+1) for i in range(n+1)]
        print 'steps: {}'.format(drop_chess(n, k, mx))
    print 'steps 2: {}'.format(drop_chess_2(n, k))
    print 'steps 3: {}'.format(drop_chess_3(n, k))

def log2n(n):
    r = -1
    while n > 0:
        r += 1
        n >>= 1
    return r

def drop_chess_3(n, k):
    if n < 1 or k < 1:
        return 0
    t = log2n(n)
    if k >= t:
        return t

    res = 0
    dp = [0] * k
    while True:
        res += 1
        prev = 0
        for i in range(k):
            tmp = dp[i]
            dp[i] += (prev + 1)
            prev = tmp
            if dp[i] >= n:
                return res

def drop_chess_2(n, k):
    if n == 0 or k == 0:
        return 0
    elif k == 1:
        return n

    A = [i for i in range(n+1)]
    B = [0 for i in range(n+1)]
    for j in range(2, k+1):
        for i in range(1, n+1):
            M = 0x7fffffff
            for p in range(0, i):
                M = min(M, max(A[p], B[i-1-p]))
            B[i] = M + 1
        T = A
        A = B
        B = T
    return A[-1]

def main():
    '''丢棋子问题'''
    test(10, 1)
    test(1, 2)
    test(1, 3)
    test(3, 2)
    test(105, 2)
    test(150, 4)
    test(150, 5)
    test(200, 3)
    test(500, 3)
    test(1500, 4)
    test(1500, 3)
    test(1500, 2)
    test(1500, 1)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
