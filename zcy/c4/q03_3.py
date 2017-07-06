#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def min_com(arr, k):
    return do_min_com(arr, 0, k)

def do_min_com(arr, i, k):
    n = len(arr)
    if i == n:
        return 0 if k == 0 else -1

    num = 0x7fffffff
    res = k
    j = 0
    while res >= 0:
        r = do_min_com(arr, i+1, res)
        if r >= 0:
            num = min(num, j+r)
        j += 1
        res -= arr[i]
    return num if num < 0x7fffffff else -1

def min_cost_2(arr, k):
    n = len(arr)
    dp = [0] * (k+1)

    for i in range(0, k+1):
        if i % arr[0] == 0:
            dp[i] = i / arr[0]
        else:
            dp[i] = 0x7fffffff

    for i in range(1, n):
        for j in range(k, 0, -1):
            num = dp[j]
            times = 1
            while j - arr[i] * times >= 0:
                num = min(num, times + dp[j-arr[i]*times])
                times += 1
            dp[j] = num

    return dp[k] if dp[k] < 0x7fffffff else -1

def min_cost_3(arr, k):
    n = len(arr)
    dp = [0] * (k+1)

    for i in range(0, k+1):
        if i % arr[0] == 0:
            dp[i] = i / arr[0]
        else:
            dp[i] = 0x7fffffff

    for i in range(1, n):
        for j in range(1, k+1, 1):
            if j >= arr[i]:
                dp[j] = min(dp[j], dp[j-arr[i]]+1)

    return dp[k] if dp[k] < 0x7fffffff else -1


def test(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    if k <= 200:
        print 'min com 1: {}'.format(min_com(arr, k))
    print 'min com 2: {}'.format(min_cost_2(arr, k))
    print 'min com 3: {}'.format(min_cost_3(arr, k))

def main():
    '''换钱的最少货币数'''
    test([5,2,3], 20)
    test([5,2,3], 0)
    test([3,5], 2)
    test([1,2,5,10,11,15,19], 87)
    test([1,2,5,10,14,17,23], 137)
    test([1,2,5,10,20,25,50,100], 180)
    test([1,2,5,10,20,35,50,63,89,100], 8379)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
