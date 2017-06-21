#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def non_min_sum(arr):
    n = len(arr)
    Sum = sum(arr)
    Min = min(arr)
    dp = [False] * (Sum+1)
    dp[0] = True

    for i in range(n):
        for j in range(Sum, arr[i] - 1, -1):
            if dp[j-arr[i]]:
                dp[j] = True

    for i in range(Min, Sum + 1):
        if not dp[i]:
            return i

    return Sum + 1

def non_min_sum2(arr):
    n = len(arr)
    arr.sort()
    r = 0
    for i in range(n):
        if arr[i] <= r + 1:
            r += arr[i]
        else:
            return r + 1
    return r + 1

def test(arr):
    print 'arr: {}'.format(arr)
    print 'non_min_sum: {}'.format(non_min_sum(arr))

def test2(arr):
    print 'arr: {}'.format(arr)
    print 'non_min_sum: {}'.format(non_min_sum2(arr))

def main():
    '''正数数组的最小不可组成和'''
    test([3,2,5])
    test([1,2,4])
    test2([1,2,4])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
