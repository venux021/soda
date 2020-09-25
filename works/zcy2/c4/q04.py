#!/usr/bin/env python3
import itertools
import sys

from sodacomm.tools import testwrapper

def charge_method_count(arr, total):
    n = len(arr)
    dp = [[0] * (total+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    j = 1
    k = arr[0]
    while k <= total:
        dp[0][k] = 1
        j += 1
        k += arr[0]
    for i, j in itertools.product(range(1,n), range(1,total+1)):
        if j >= arr[i]:
            dp[i][j] = dp[i-1][j] + dp[i][j-arr[i]]
        else:
            dp[i][j] = dp[i-1][j]
    print(dp)
    return dp[n-1][total]

@testwrapper
def test(arr, n):
    print(arr, n)
    print(charge_method_count(arr, n))

def main():
    test([5,10,25,1], 0)
    test([5,10,25,1], 15)
    test([3,5], 2)

if __name__ == '__main__':
    main()
