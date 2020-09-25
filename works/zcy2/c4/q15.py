#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def least_jump(arr):
    n = len(arr)
    if n < 2:
        return 0
    elif n == 2:
        return 1
    dp = [sys.maxsize] * n
    dp[-1] = 0
    dp[-2] = 1
    for i in range(n-3, -1, -1):
        for j in range(i+1, i+arr[i]+1):
            dp[i] = min(dp[i], dp[j] + 1)
    return dp[0]

def least_jump2(arr):
    cur_dist = 0
    next_dist = 0
    jump = 0
    n = len(arr)
    for i in range(n):
        if i > cur_dist:
            jump += 1
            cur_dist = next_dist
        next_dist = max(next_dist, i + arr[i])
    return jump

@testwrapper
def test(arr):
    print(arr)
    print(least_jump(arr), least_jump2(arr))

def main():
    test([3,2,3,1,1,4])

if __name__ == '__main__':
    main()
