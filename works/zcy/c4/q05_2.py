#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def up_seq(arr):
    n = len(arr)
    dp = [0] * n
    dp[0] = 1
    ends = [0] * n
    right = 0
    ends[0] = arr[0]

    for i in range(1, n):
        k = locate(ends, right, arr[i])
        dp[i] = k + 1
        if dp[i]-1 <= right:
            ends[dp[i] - 1] = min(ends[dp[i]-1], arr[i])
        else:
            ends[right+1] = arr[i]
            right += 1

    for i in range(n-1, -1, -1):
        if dp[i] == right + 1:
            break

    r = [0] * (right+1)
    r[right] = arr[i]
    p = right-1
    j = i - 1
    while j >= 0:
        if arr[j] < arr[i] and dp[j] == dp[i] - 1:
            r[p] = arr[j]
            p -= 1
            i = j
        j -= 1

    return r

def locate(ends, right, k):
    low = 0
    high = right
    while low <= high:
        mid = (low + high) / 2
        if ends[mid] >= k:
            high = mid - 1
        else:
            low = mid + 1
    return low

def test(arr):
    print 'arr: {}'.format(arr)
    print 'up seq: {}'.format(up_seq(arr))

def main():
    '''最长递增子序列'''
    test([2,1,5,3,6,4,8,9,7])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
