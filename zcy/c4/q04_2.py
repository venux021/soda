#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def exch(arr, i, k):
    n = len(arr)
    if i == n:
        return 1 if k == 0 else 0

    res = 0
    while k >= 0:
        res += exch(arr, i+1, k)
        k -= arr[i]
    return res

def exchange(arr, k):
    if k > 200:
        return 'Too big'
    return exch(arr, 0, k)

def test(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    print 'exchange 1: {}'.format(exchange(arr, k))
    print 'exchange 2: {}'.format(exchange2(arr, k))
    print 'exchange 3: {}'.format(exchange3(arr, k))

def exchange3(arr, k):
    n = len(arr)
    dp = [0] * (k+1)

    for i in range(k+1):
        if i % arr[0] == 0:
            dp[i] = 1

    for i in range(1, n):
        for j in range(1, k+1):
            if j >= arr[i]:
                dp[j] += dp[j-arr[i]]

    return dp[k]

def exchange2(arr, k):
    n = len(arr)
    dp = [0] * (k+1)

    for i in range(k+1):
        if i % arr[0] == 0:
            dp[i] = 1

    for i in range(1, n):
        for j in range(k, 0, -1):
            r = j
            res = 0
            while r >= 0:
                res += dp[r]
                r -= arr[i]
            dp[j] = res

    return dp[k]

def main():
    '''换钱的方法数'''
    test([5,10,25,1], 15)
    test([5,10,25,1], 0)
    test([3,5], 2)
    test([1,2,5,10,20,50,100], 180)
    test([1,2,5,10,20,50,100], 3180)
    test([1,2,5,10,20,50,100], 13180)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
