#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

def find_k(arr, k):
    n = len(arr)
    return select(arr, 0, n-1, k-1)

def select(arr, start, end, k):
    if start == end:
        return arr[start]

    mid = get_median_m(arr, start, end)

    p = partition(arr, start, end, mid)
    print('p:', p)

    if p == k:
        return arr[k]
    elif p < k:
        return select(arr, p+1, end, k)
    else:
        return select(arr, start, p-1, k)

def get_median_m(arr, start, end):
    i = start
    n = end - start + 1
    k = n // 5
    if n % 5:
        k += 1
    r = [0] * k
    c = 0
    while i+5 <= end+1:
        insert_sort(arr, i, i+4)
        r[c] = arr[i+2]
        c += 1
        i += 5

    if i <= end:
        insert_sort(arr, i, end)
        L = end-i+1
        r[c] = arr[i+L//2]

    return select(r, 0, k-1, k//2)

def insert_sort(arr, start, end):
    for j in range(start+1, end+1):
        i = j
        k = arr[j]
        while i > 0 and arr[i-1] > k:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = k

def partition(arr, start, end, pivot):
    i = start - 1
    j = end+1
    m = start
    while m < j:
        if arr[m] > pivot:
            j -= 1
            if m < j:
                swap(arr, j, m)
        elif arr[m] < pivot:
            i += 1
            if i < m:
                swap(arr, i, m)
            m += 1
        else:
            m += 1
    return i + 1

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def test(n, k):
    arr = [i for i in range(1, n+1)]
    random.shuffle(arr)
    p = find_k(arr, k)
    print('Total {}, No {}: {}'.format(n, k, p))

def main():
    '''组5取中法找出第k小的数字'''
    test(10, 3)
    test(20, 16)
    test(30, 22)
    test(40, 1)
    test(40, 40)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
