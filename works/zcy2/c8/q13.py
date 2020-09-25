#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def less_sum_1(arr):
    n = len(arr)
    s = 0
    for i in range(1, n):
        t = 0
        for j in range(0, i):
            if arr[j] <= arr[i]:
                t += arr[j]
        s += t
    return s

def less_sum_2(arr):
    n = len(arr)
    temp = [0] * n
    s = merge_sort(arr, 0, n-1, temp)
#    print(arr)
    return s

def merge_sort(arr, i, j, temp):
    if i == j:
        return 0
    mid = (i + j) // 2
    left = merge_sort(arr, i, mid, temp)
    right = merge_sort(arr, mid + 1, j, temp)
    s = do_merge(arr, i, mid, mid + 1, j, temp)
    return left + right + s

def do_merge(arr, a1, a2, b1, b2, temp):
    i, j = a1, b1
    c = a1
    s = 0
    while i <= a2 and j <= b2:
        if arr[i] <= arr[j]:
            temp[c] = arr[i]
            s += (b2-j+1) * arr[i]
            i += 1
        else:
            temp[c] = arr[j]
            j += 1
        c += 1
    while i <= a2:
        temp[c] = arr[i]
        c += 1
        i += 1
    while j <= b2:
        temp[c] = arr[j]
        c += 1
        j += 1
    arr[a1:b2+1] = temp[a1:b2+1]
    return s

@testwrapper
def test(arr):
    print(arr)
    print(less_sum_1(arr))
    print(less_sum_2(arr))

def main():
    test([1,3,5,2,4,6])
    test([5,1,2,7,8,3,8,4,1,9,3,6,4])

if __name__ == '__main__':
    main()
