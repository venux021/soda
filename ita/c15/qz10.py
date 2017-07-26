#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

MIN = -0x7fffffff

def brute_force(v, fee, trans_fee, capital):
    m = MIN
    for i in range(len(v[0])):
        m = max(m, _bf(v, 0, i, fee, trans_fee, capital * (1+v[0][i])))
    return m

def _bf(v, year, c, fee, trans_fee, capital):
    if year == len(v) - 1:
        return capital * (1 + v[year][c])

    m = MIN
    fruit = capital * (1 + v[year][c])
    for i in range(len(v[0])):
        if i == c:
            m = max(m, _bf(v, year+1, i, fee, trans_fee, fruit - fee))
        else:
            m = max(m, _bf(v, year+1, i, fee, trans_fee, fruit - trans_fee))
    return m

def brute_force_2(v, fee, trans_fee, capital):
    m = MIN
    for i in range(len(v[0])):
        m = max(m, _bf2(v, len(v)-1, i, fee, trans_fee, capital))
    return m

def _bf2(v, year, c, fee, trans_fee, capital):
    if year == 0:
        return capital * (1 + v[0][c])

    m = MIN
    k = v[year][c]
    for i in range(len(v[0])):
        if i == c:
            m = max(m, (_bf2(v, year-1, i, fee, trans_fee, capital)-fee) * (1 + k))
        else:
            m = max(m, (_bf2(v, year-1, i, fee, trans_fee, capital)-trans_fee) * (1 + k))
    return m

#def with_dp(v, fee, trans_fee, capital):
#    m = len(v)
#    n = len(v[0])
#    dp = [[0] * n for i in range(m)]
#    plan = [[-1] * n for i in range(m)]
#
#    for j in range(n):
#        dp[m-1][j] = v[m-1][j]
#    for i in range(m-2, 

def show_invest_plan(v, fee, trans_fee, capital):
    print('brute force 1:', brute_force(v, fee, trans_fee, capital))
    print('brute force 2:', brute_force_2(v, fee, trans_fee, capital))

def test(num_invest, num_years, fee, trans_fee, capital):
    v = [[random.uniform(0.05,0.15) for i in range(num_invest)] for j in range(num_years)]
    show_invest_plan(v, fee, trans_fee, capital)

def main():
    '''投资策略规划'''
    test(5, 10, 100, 200, 10000)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
