#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

def show_optimal_recur(capacity, weight, value):
    n = len(weight)
    uprice = [value[i] // weight[i] for i in range(n)]
    print('brute force:', _sor(capacity, 0, weight, value, uprice))

def _sor(capacity, i, weight, value, uprice):
    n = len(weight)
    if i == n:
        return 0

    v = 0
    for k in range(min(capacity, weight[i])+1):
        v = max(v, uprice[i]*k + _sor(capacity-k, i+1, weight, value, uprice))
    return v

def show_optimal_dp(capacity, weight, value):
    n = len(weight)
    uprice = [value[i] // weight[i] for i in range(n)]
    dp = [[0] * (capacity+1) for i in range(n)]
    select = [[0] * (capacity+1) for i in range(n)]

    for i in range(n):
        for j in range(capacity+1):
            for k in range(min(j,weight[i])+1):
                K = dp[i-1][j-k] + k*uprice[i]
                if K > dp[i][j]:
                    dp[i][j] = K
                    select[i][j] = k

    print('dynamic prog:', dp[n-1][capacity])
    s = []
    R = capacity
    for i in range(n-1, -1, -1):
        p = select[i][R]
        s.append(p)
        R -= p
    solution = list(zip(uprice, weight, s[::-1]))
    solution.sort(key = lambda x: -x[0])
    print(solution)

def show_optimal_greedy(capacity, weight, value):
    n = len(weight)
    uprice = [value[i] // weight[i] for i in range(n)]
    T = list(zip(uprice, weight, value))
    T.sort(key = lambda x: -x[0])
    uprice, weight, value = zip(*T)

    print('for greedy:')
    v = 0
    for i in range(n):
        if capacity >= weight[i]:
            capacity -= weight[i]
            v += value[i]
            print('u:{} w:{} t:{}'.format(uprice[i], weight[i], weight[i]))
        else:
            v += uprice[i] * capacity
            print('u:{} w:{} t:{}'.format(uprice[i], weight[i], capacity))
            break
    print('greedy:', v)

def test(n):
    uprice = [random.randint(1,10) for i in range(n)]
    weight = [random.randint(5,35) for i in range(n)]
    value = [uprice[i] * weight[i] for i in range(n)]
    capacity = sum(weight) * 6 // 7
    if n <= 5:
        show_optimal_recur(capacity, weight, value)
    show_optimal_dp(capacity, weight, value)
    show_optimal_greedy(capacity, weight, value)

def main():
    '''动态规划解分数背包问题'''
    test(5)
    test(20)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
