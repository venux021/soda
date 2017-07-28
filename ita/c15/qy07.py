#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random
import functools

def optimal_value(t, p, d):
    n = len(t)
    arr = [i for i in range(n)]
    return _ov(arr, 0, t, p, d, 0)

def _ov(arr, s, t, p, d, T):
    n = len(arr)
    if s == n:
        return 0

    v = 0
    for i in range(s, n):
        swap(arr, s, i)
        if t[arr[s]] + T <= d[arr[s]]:
            v = max(v, p[arr[s]] + _ov(arr, s+1, t, p, d, T+t[arr[s]]))
        else:
            v = max(v, _ov(arr, s+1, t, p, d, T))
        swap(arr, s, i)
    return v

def swap(arr, i, j):
    if i != j:
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t

def show_opt_dp(t, p, d):
    L = list(zip(t, p, d))
    L.sort(key = lambda x: x[2])
    t, p, d = zip(*L)
    
    n = len(t)
    T = d[-1]

    dp = [0] * (T+1)
    select = [[False] * (T+1) for i in range(n)]

    for i in range(t[0], d[0]+1):
        dp[i] = p[0]
        select[0][i] = True

    first = min(t)
    for i in range(1, n):
        for j in range(d[i], first - 1, -1):
            a = dp[min(j,d[i-1])]
            if j >= t[i]:
                b = p[i] + dp[min(j-t[i], d[i-1])]
                if b > a:
                    select[i][j] = True
            else:
                b = 0
            dp[j] = max(a, b)

    print('from dp:', dp[T])
    for i in range(n):
        if select[i][d[i]]:
            print(i, end = ' ')
    print()

def show_optimal(t, p, d):
    n = len(t)
    L = list(zip(t, p, d))
    L.sort(key = lambda x: x[2])
    t, p, d = zip(*L)

    print('show_optimal 1:', _so(0, t, p, d, 0))
    print('show_optimal 2:', _so2(n-1, t, p, d, d[n-1]))

def _so2(s, t, p, d, T):
    if s == 0:
        return p[0] if T >= t[0] else 0

    a = _so2(s-1, t, p, d, min(d[s-1],T))

    if T >= t[s]:
        b = _so2(s-1, t, p, d, min(T-t[s],d[s-1])) + p[s]
        return max(a, b)
    else:
        return a

def _so(s, t, p, d, T):
    n = len(t)
    if s == n:
        return 0

    if t[s] + T <= d[s]:
        a = p[s] + _so(s+1, t, p, d, T + t[s])
    else:
        a = 0
    b = _so(s+1, t, p, d, T)
    return max(a, b)

def test(n):
    t = [random.randint(5,100) for i in range(n)]
    p = [random.randint(10,300) for i in range(n)]
    T = sum(t) * 5 // 6
    d = [0] * n
    for i in range(n):
        d[i] = random.randint(t[i], T)
#    t,p,d = [45, 45, 26],[123, 168, 90],[84, 57, 30]
    if n <= 10:
        print(optimal_value(t, p, d))
    show_optimal(t, p, d)
    show_opt_dp(t, p, d)
    print()

def main():
    '''达到最高效益的调度'''
    test(3)
    test(7)
    test(20)
    test(24)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
