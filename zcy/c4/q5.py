#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def mss(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return genss(arr, dp)

def mss_2(arr):
    n = len(arr)
    dp = [1] * n
    end = [0] * n
    end[0] = arr[0]
    R = 0

    for i in range(1, n):
        a = 0
        b = R
        while a <= b:
            mid = (a + b) / 2
            if arr[i] >= end[mid]:
                a = mid + 1
            else:
                b = mid - 1

        end[a] = arr[i]
        dp[i] = a + 1

        if a > R:
            R += 1

    return genss(arr, dp)

def genss(arr, dp):
    mi = 0
    for i in range(1, len(dp)):
        if dp[i] > dp[mi]:
            mi = i

    r = [arr[mi]]
    L = dp[mi] - 1
    for i in range(mi - 1, -1, -1):
        if dp[i] == L and arr[i] < arr[mi]:
            r.append(arr[i])
            L -= 1
            if L == 0:
                break
            mi = i
    r.reverse()
    return r

def test(arr):
    print 'arr: {}'.format(arr)
    print 'mss: {}'.format(mss(arr))
    print 'mss2: {}'.format(mss_2(arr))

def main():
    '''最长递增子序列'''
    test([2,1,5,3,6,4,8,9,7])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
