#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

def qselect(arr, start, end, k):
    n = end - start + 1
    if n <= 5:
        insertion_sort(arr, start, end)
        return

    pivot = median3(arr, start, end)
    i = start
    j = end - 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            swap(arr, i, j)
        else:
            break

    swap(arr, end-1, i)

    if i < k:
        qselect(arr, i + 1, end, k)
    elif i > k:
        qselect(arr, start, i - 1, k)

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def median3(arr, start, end):
    mid = (start + end) // 2
    if arr[start] > arr[end]:
        swap(arr, start, end)
    if arr[start] > arr[mid]:
        swap(arr, start, mid)
    if arr[mid] > arr[end]:
        swap(arr, mid, end)
    swap(arr, mid, end-1)
    return arr[end-1]

def insertion_sort(arr, start, end):
    for j in range(start+1, end+1):
        temp = arr[j]
        i = j
        while i > start:
            if arr[i-1] > temp:
                arr[i] = arr[i-1]
                i -= 1
            else:
                break
        if i < j:
            arr[i] = temp

def kth_element(arr, k):
    n = len(arr)
    if k <= n and k > 0:
        qselect(arr, 0, n-1, k-1)
        return arr[k-1]
    else:
        return None

def std_kth(arr, k):
    n = len(arr)
    if k <= n and k > 0:
        arr.sort()
        return arr[k-1]
    else:
        return None

def test(n, k):
    arr = [random.randint(1,1000) for i in range(n)]
    if k == 20:
        print('original:', arr)
    k1 = kth_element(arr, k)
    k2 = std_kth(arr, k)
    if n < 30:
        arr.sort()
        print(arr, k, k1, k2)
    else:
        print(n, k, k1, k2)

def test2(arr, k):
    k1 = kth_element(arr, k)
    arr.sort()
    print(arr)
    print(arr[k-1], k1)

def main():
    '''选择无序数组排序后第k个数字'''
    test(20, 6)
    test(20, 0)
    test(20, 21)
    test(20, 1)
    test(20, 20)
    test(100, 9)
    test(10000, 93)
    test2([35, 60, 186, 382, 421, 452, 466, 474, 481, 518, 586, 591, 642, 665, 837, 857, 874, 882, 967, 968], 20)
    test2([152, 58, 641, 530, 694, 620, 566, 788, 609, 545, 572, 851, 339, 720, 241, 906, 177, 236, 150, 818], 20)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
