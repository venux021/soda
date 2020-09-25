#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

MIN = -0x7fffffff


def brute_force(F, V, x, pos):
    if pos < 0:
        return 0
    p = len(F[0])
    r = MIN
    for i in range(p):
        if x >= F[pos][i]:
            r = max(r, brute_force(F,V,x - F[pos][i], pos-1) + V[pos][i])
    return r

def show_optimal_plan(F, V, x):
    n = len(F)
    p = len(F[0])
    row = n
    col = x + 1

    dp = [[0] * col for i in range(row)]
    for i in range(p):
        dp[0][F[0][i]] = max(dp[0][F[0][i]], V[0][i])

    m = 0
    for i in range(col):
        m = max(m, dp[0][i])
        dp[0][i] = m

    for i in range(1, row):
        for j in range(col):
            mx = 0
            for k in range(p):
                if j >= F[i][k]:
                    mx = max(mx, dp[i-1][j - F[i][k]] + V[i][k])
            dp[i][j] = mx

    print(dp[n-1][x])

def show_optimal_plan_2(F, V, x):
    n = len(F)
    p = len(F[0])
    row = n
    col = x + 1

    dp = [0] * col
    act = [[-1] * col for i in range(row)]
    for i in range(p):
        if V[0][i] > dp[F[0][i]]:
            dp[F[0][i]] = V[0][i]
            act[0][F[0][i]] = i            

    m = 0
    mi = -1
    for i in range(col):
        if dp[i] >= m:
            m = dp[i]
            mi = i
        else:
            dp[i] = m
            act[0][i] = act[0][mi]

    for i in range(1, row):
        for j in range(col-1, -1, -1):
            mx = 0
            for k in range(p):
                if j >= F[i][k]:
#                    mx = max(mx, dp[j - F[i][k]] + V[i][k])
                    yy = dp[j - F[i][k]] + V[i][k]
                    if yy > mx:
                        mx = yy
                        act[i][j] = k
            dp[j] = mx

    remain = x
    players = []
    for i in range(n-1, -1, -1):
        p = act[i][remain]
        players.append(p)
        remain -= F[i][p]

    print('total: {}, remain: {}'.format(dp[x], remain))
    print('player:', players)

def test(n, p, x):
    d = x/n/4
    down = int(x/n - d)
    up = int(x/n + d)
    F = [[random.randint(down, up) for i in range(p)] for j in range(n)]
    V = [[random.randint(50, 150) for i in range(p)] for j in range(n)]

    if n <= 10 and p < 6 or n < 6:
        n = len(F)
        print(brute_force(F, V, x, n-1))

    show_optimal_plan(F, V, x)
    show_optimal_plan_2(F, V, x)

def main():
    '''签约棒球自由球员'''
    test(5, 4, 49)
    test(9, 5, 300)
    test(5, 15, 400)
    test(10, 5, 500)
    test(20, 40, 5000)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
