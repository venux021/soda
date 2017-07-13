#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def sort(arr):
    qsort(arr, 0, len(arr) - 1)
    return arr

def qsort(arr, start, end):
    if end - start < 5:
        ins_sort(arr, start, end)
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
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
        else:
            break

    t = arr[i]
    arr[i] = arr[end-1]
    arr[end-1] = t

    qsort(arr, start, i-1)
    qsort(arr, i+1, end)

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def median3(arr, start, end):
    mid = (start + end) >> 1
    if arr[start] > arr[mid]:
        swap(arr, mid, start)
    if arr[start] > arr[end]:
        swap(arr, start, end)
    if arr[mid] > arr[end]:
        swap(arr, mid, end)
    swap(arr, mid, end-1)
    return arr[end-1]

def ins_sort(arr, start, end):
    if end - start <= 1:
        return
    for j in range(start+1, end+1):
        k = arr[j]
        i = j - 1
        while arr[i] > k and i >= start:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = k

def test(arr):
    print('origin:', arr)
    print('sorted:', sort(arr))

def main():
    '''快速排序'''
    test([4,2,1,7,3,1,6,3,9,6,3,2,7,5,1,4,8,6,3,5,8])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
