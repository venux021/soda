#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def card2(arr):
    n = len(arr)
    dpf = [[0] * n for i in range(n)]
    dps = [[0] * n for i in range(n)]
    for i in range(n):
        dpf[i][i] = arr[i]
    for k in range(1, n):
        i = 0
        j = k
        while i < n and j < n:
            dpf[i][j] = max(arr[i] + dps[i+1][j], arr[j] + dps[i][j-1])
            dps[i][j] = min(dpf[i+1][j], dpf[i][j-1])
            i += 1
            j += 1
    return max(dpf[0][n-1], dps[0][n-1])

def card(arr):
    total = sum(arr)
    score = f(arr, 0, len(arr)-1)
    return max(score, total - score)

def f(arr, i, j):
    if i == j:
        return arr[i]
    return max(arr[i] + s(arr, i+1, j), arr[j] + s(arr, i, j-1))

def s(arr, i, j):
    if i == j:
        return 0
    return min(f(arr, i+1, j), f(arr, i, j-1))

@testwrapper
def test(arr):
    print(arr)
    print(card(arr), card2(arr))

def main():
    test([1,2,100,4])
    test([1,100,2])

if __name__ == '__main__':
    main()
