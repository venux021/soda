#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random
import time

def mink(arr, k):
    n = len(arr)
    i = nth_element(arr, 0, n-1, k-1)
    r = filter(lambda x: x < i, arr)
    return r + ([i] * (k - len(r)))

def nth_element(arr, i, j, k):
    if i == j:
        return arr[i]

    piv = get_median_plus(arr, i, j)
    x = partition(arr, i, j, piv)
    if x == k:
        return arr[x]
    elif x < k:
        return nth_element(arr, x + 1, j, k)
    else:
        return nth_element(arr, i, x - 1, k)

def partition(arr, i, j, piv):
    low = i - 1
    high = j + 1
    c = i
    while c < high:
        if arr[c] == piv:
            c += 1
        elif arr[c] > piv:
            high -= 1
            swap(arr, c, high)
        else:
            low += 1
            swap(arr, low, c)
            c += 1
    return low + 1

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def get_median_plus(arr, i, j):
    r, p = divmod(j-i+1, 5)
    if p > 0:
        r += 1
    md = [0] * r

    for k in range(i, j+1, 5):
        md[(k-i)/5] = median(arr, k, min(j, k + 4))

    return nth_element(md, 0, r - 1, r/2)

def median(arr, i, j):
    insert_sort(arr, i, j)
    if (j - i) & 1 == 0:
        return arr[(i+j)/2]
    else:
        return arr[(i+j)/2+1]

def insert_sort(arr, start, end):
    for i in range(1, end+1):
        t = arr[i]
        j = i - 1
        while j >= start:
            if arr[j] > t:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break
        arr[j+1] = t

def gen_arr(n, i, j):
    return [random.randint(i, j) for k in range(n)]

def test(n, k):
    if isinstance(n, int):
        arr = gen_arr(n, 1, n - n/4)
    else:
        arr = n
    print 'arr: {}, k: {}'.format(arr, k)
    r = mink(arr, k)
    r.sort()
    print 'mink: {}'.format(r)
    arr.sort()
    print 'sort mink: {}'.format(arr[:k])

def main():
    '''找到无序数组中最小的k个数'''
    test(10, 4)
    test(20, 15)
    test(40, 7)
    test([5, 19, 8, 30, 13, 15, 2, 13, 12, 2, 23, 12, 28, 28, 11, 10, 20, 7, 25, 3, 8, 24, 18, 26, 28, 18, 16, 15, 4, 14, 17, 20, 6, 11, 26, 24, 10, 23, 4, 3], 7)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
