#!/usr/bin/env python3
import itertools
import sys

from sodacomm.tools import testwrapper

def min_money_count(arr, sum_):
    n = len(arr)
    dp = [[sys.maxsize] * (sum_ + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 0
    j = 0
    while j * arr[0] <= sum_:
        dp[0][j*arr[0]] = j
        j += 1
    for i, j in itertools.product(range(1,n), range(1, sum_ + 1)):
        if j < arr[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-arr[i]] + 1)
    r = dp[n-1][sum_]
    return r if r < sys.maxsize else -1

def min_money_count2(arr, sum_):
    n = len(arr)
    dp = [[sys.maxsize] * (sum_ + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 0
    if arr[0] <= sum_:
        dp[0][arr[0]] = 1
    for i, j in itertools.product(range(1,n), range(1, sum_+1)):
        if j < arr[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-arr[i]] + 1)
    r = dp[n-1][sum_]
    return r if r < sys.maxsize else -1

@testwrapper
def test(arr, n):
    print(arr, n)
    print(min_money_count(arr, n))

@testwrapper
def test2(arr, n):
    print(arr, n)
    print(min_money_count2(arr, n))

def main():
    test2([5,2,3], 20)
    test2([5,2,5,3], 10)
    test2([5,2,5,3], 15)
    test2([5,2,5,3], 0)
    test([5,2,3], 20)
    test([5,2,3], 0)
    test([3,5], 2)

if __name__ == '__main__':
    main()
