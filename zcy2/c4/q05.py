#!/usr/bin/env python3
import itertools
import random
import sys

from sodacomm.tools import testwrapper

def longest_ascend_seq_1(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1,n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    buf = []
    target = max(dp)
    i = dp.index(target)
    buf.append(arr[i])
    for j in range(i-1, -1, -1):
        if dp[j] == dp[i] - 1 and arr[j] < arr[i]:
            buf.append(arr[j])
            i = j
    return list(reversed(buf))

def longest_ascend_seq_2(arr):
    n = len(arr)
    dp = [1] * n
    ends = [0] * n
    right = 0
    ends[0] = arr[0]

    for i in range(1, n):
        k = search(ends, right, arr[i])
        if k > right:
            right += 1
        ends[k] = arr[i]
        dp[i] = k + 1

    buf = []
    target = max(dp)
    i = dp.index(target)
    buf.append(arr[i])
    for j in range(i-1, -1, -1):
        if dp[j] == dp[i] - 1 and arr[j] < arr[i]:
            buf.append(arr[j])
            i = j
    return list(reversed(buf))

def search(ends, right, x):
    L = 0
    R = right
    while L <= R:
        mid = (L+R)//2
        if x == ends[mid]:
            return mid
        elif x < ends[mid]:
            R = mid - 1
        else:
            L = mid + 1
    return L

@testwrapper
def test(arr):
    print(arr)
    print(longest_ascend_seq_1(arr))
    print(longest_ascend_seq_2(arr))

def main():
    test([2,1,5,3,6,4,8,9,7])
    test([3, 6, 7, 12, 14, 1, 18, 2, 16, 8, 17, 11, 13, 4, 15, 5, 10, 19, 9])
    a = [i for i in range(1, 20)]
    random.shuffle(a)
    test(a)

if __name__ == '__main__':
    main()
