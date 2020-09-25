#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def partition_1(arr, pred):
    n = len(arr)
    i, j = 0, n-1
    while i < j:
        while pred(arr[i]):
            i += 1
            if i == j:
                return i+1 if pred(arr[i]) else i
        while not pred(arr[j]):
            j -= 1
            if i == j:
                return i+1 if pred(arr[i]) else i
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return i if not pred(arr[i]) else i + 1

def partition_2(arr, pred):
    n = len(arr)
    i, j = 0, n
    while i != j:
        while pred(arr[i]):
            i += 1
            if i == j:
                return i
        j -= 1
        if i == j:
            return i
        while not pred(arr[j]):
            j -= 1
            if i == j:
                return i
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return i

def partition_3(arr, pred):
    n = len(arr)
    i, j = -1, 0
    while j < n:
        if pred(arr[j]):
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1
    return i + 1

def partition_4(arr, pivot):
    if pivot not in arr:
        return -1
    i = arr.index(pivot)
    if i > 0:
        arr[0], arr[i] = arr[i], arr[0]

    n = len(arr)
    low, high = 0, n-1
    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

        while low < high and arr[low] <= pivot:
            low += 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    return low

def partition_5(arr, pivot):
    n = len(arr)
    low = -1
    p = 0
    high = n
    while p < high:
        if arr[p] < pivot:
            low += 1
            if low != p:
                arr[p], arr[low] = arr[low], arr[p]
            p += 1
        elif arr[p] > pivot:
            high -= 1
            if high != p:
                arr[p], arr[high] = arr[high], arr[p]
        else:
            p += 1
    return low + 1

@testwrapper
def test(arr, k):
    pred = lambda x: x < k
    print(arr, k)

    a1 = arr[:]
    i1 = partition_1(a1, pred)
    display(a1, i1)

    a2 = arr[:]
    i2 = partition_2(a2, pred)
    display(a2, i2)

    a3 = arr[:]
    i3 = partition_3(a3, pred)
    display(a3, i3)

    a4 = arr[:]
    i4 = partition_4(a4, k)
    display(a4, i4)

    a5 = arr[:]
    i5 = partition_5(a5, k)
    display(a5, i5)

def display(a, i):
    if i < len(a):
        a[i] = f'{a[i]}*'
        print(i, a)
    else:
        print(i, a, '*')

def main():
    test([5,4,3,2,1], 0)
    test([5,4,3,2,1], 5)
    test([5,4,3,2,1], 2)
    test([5,4,3,2,1], 4)

if __name__ == '__main__':
    main()
