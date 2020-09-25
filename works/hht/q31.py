#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def test(arr):
    print('arr: {}'.format(arr))
    print('max sum: {}'.format(max_sum(arr)))

def max_sum(arr):
    n = len(arr)
    dp = [0] * n

    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(arr[i], arr[i] + dp[i-1])

    return max(dp)

def main():
    '''连续子数组最大和'''
    test([1,-2,3,10,-4,7,2,-5])
    test([-10,-6,-4,-2,-3])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
