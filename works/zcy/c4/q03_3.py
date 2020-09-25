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

def test2(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    print 'min cost 1: {}'.format(min01_cost_1(arr, k))
    print 'min cost 2: {}'.format(min01_cost_2(arr, k))

def min01_cost_1(arr, k):
    return do_min01_cost(arr, 0, k)

def do_min01_cost(arr, p, k):
    n = len(arr)
    if p == n:
        return 0 if k == 0 else -1
    elif k == 0:
        return 0
    elif k < 0:
        return -1

    x = do_min01_cost(arr, p+1, k-arr[p])
    y = do_min01_cost(arr, p+1, k)
    if x == -1 and y == -1:
        return -1
    elif x == -1:
        return y
    elif y == -1:
        return x + 1
    else:
        return min(x+1, y)

def min01_cost_2(arr, k):
    n = len(arr)
    dp = [0] * (k+1)

    for i in range(1,k+1):
        if arr[0] == k:
            dp[i] = 1
        else:
            dp[i] = 0x7fffffff

    for i in range(1, n):
        for j in range(k, 0, -1):
            if j >= arr[i]:
                dp[j] = min(dp[j], dp[j-arr[i]]+1)

    return dp[k] if dp[k] < 0x7fffffff else -1

def main():
    '''换钱的最少货币数'''
#    test([5,2,3], 20)
#    test([5,2,3], 0)
#    test([3,5], 2)
#    test([1,2,5,10,11,15,19], 87)
#    test([1,2,5,10,14,17,23], 137)
#    test([1,2,5,10,20,25,50,100], 180)
#    test([1,2,5,10,20,35,50,63,89,100], 8379)
    test2([1,5,3,1,3,5,3,4,5,1,1], 21)
    test2([3,2,1,2,2,6,2,2,9], 10)
    test2([3,6,2,4,5,6,7,8,2,4,6,7,8,3,1], 37)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
