#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

MIN = -0x7fffffff

def show_plan(capacity, weight, value):
    n = len(weight)
    dp = [0] * (capacity+1)
    acc = [0] * (n+1)
    
    for i in range(n):
        acc[i] = acc[i-1] + weight[i]
    mw = min(weight)

    dp[weight[0]] = value[0]

    for i in range(1, n):
        for j in range(min(capacity, acc[i]), weight[i]-1, -1):
            a = dp[min(j,acc[i-1])]
            b = dp[min(j-weight[i], acc[i-1])] + value[i]
            dp[j] = max(a, b)

    print('with dp:', dp[capacity])

def show_full_plan(capacity, weight, value):
    n = len(weight)
    dp = [MIN] * (capacity+1)
    acc = [0] * (n+1)
    
    for i in range(n):
        acc[i] = acc[i-1] + weight[i]
    mw = min(weight)

    dp[weight[0]] = value[0]

    for i in range(1, n):
        for j in range(min(capacity, acc[i]), weight[i]-1, -1):
            if dp[j-weight[i]] > MIN:
                b = dp[j-weight[i]] + value[i]
                if b > dp[j]:
                    dp[j] = b

    print('with full dp:', dp[capacity])

def show_plan_recur(capacity, weight, value):
    n = len(weight)
    print('brute force:', _spr(capacity, n-1, weight, value))

def _spr(c, i, w, v):
    if i < 0:
        return 0

    if c >= w[i]:
        a = v[i] + _spr(c-w[i], i-1, w, v)
    else:
        a = 0

    b = _spr(c, i-1, w, v)
    return max(a, b)

def show_full_plan_recur(capacity, weight, value):
    n = len(weight)
    print('just full:', _sfpr(capacity, n-1, weight, value))

def _sfpr(c, i, w, v):
    if i < 0:
        return 0 if c == 0 else MIN

    b = _sfpr(c, i-1, w, v)
    if c >= w[i]:
        a = v[i] + _sfpr(c-w[i], i-1, w, v)
        return max(a, b)
    else:
        return b

def test(n):
    weight = [random.randint(3,40) for i in range(n)]
    value = [random.randint(100,1000) for i in range(n)]
    capacity = sum(weight) * 5 // 6
    print('total objects:', n)
    if n < 23:
        show_plan_recur(capacity, weight, value)
        show_full_plan_recur(capacity, weight, value)
    show_plan(capacity, weight, value)
    show_full_plan(capacity, weight, value)
    print('----')

def main():
    '''0/1背包问题'''
    test(10)
    test(15)
    test(21)
    test(22)
    test(40)
    test(70)
    test(100)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
