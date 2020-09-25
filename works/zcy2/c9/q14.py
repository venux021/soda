#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def all_sum(arr):
    do_all_sum(0, arr, 0)

def do_all_sum(s, arr, i):
    if i == len(arr):
        print(s)
        return
    do_all_sum(s, arr, i+1)
    do_all_sum(s+arr[i], arr, i+1)

def min_unformed_sum(arr):
    n = len(arr)
    _sum = sum(arr)
    dp = [False] * (_sum+1)
    dp[0] = True
    dp[arr[0]] = True
    limit = arr[0]
    for i in range(1, n):
        for j in range(limit, -1, -1):
            if dp[j]:
                dp[j+arr[i]] = True
        limit += arr[i]

    _min = min(arr)
    for i in range(_min+1, _sum+1):
        if not dp[i]:
            return i
    return _sum+1

def min_unformed_sum_with_1(arr):
    arr = list(sorted(arr))
    _range = 0
    for i in arr:
        if i <= _range+1:
            _range += i
        else:
            break
    return _range+1

@testwrapper
def test(arr):
    print(arr)
    print(min_unformed_sum(arr))

@testwrapper
def test2(arr):
    test(arr)
    print(min_unformed_sum_with_1(arr))

def main():
    test([3,2,5])
    test([1,2,4])
    test2([3,8,1,2])

if __name__ == '__main__':
    main()
