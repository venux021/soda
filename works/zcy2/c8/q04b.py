#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def kth_element(arr, k):
    if k < 0 or k >= len(arr):
        return 
    return select(arr, 0, len(arr)-1, k)

def select(arr, i, j, k):
    n = j - i + 1
    if n < 5:
        insertion_sort(arr, i, j)
        return arr[k]

    mid = median_of_median(arr, i, j)
    a, b = bi_partition(arr, i, j, mid)
    if k >= a and k <= b:
        return arr[a]
    elif k < a:
        return select(arr, i, a-1, k)
    else:
        return select(arr, b+1, j, k)

def bi_partition(arr, i, j, pivot):
    low = i-1
    high = j+1
    p = i
    while p < high:
        if arr[p] < pivot:
            low += 1
            if low != p:
                arr[low], arr[p] = arr[p], arr[low]
            p += 1
        elif arr[p] > pivot:
            high -= 1
            arr[p], arr[high] = arr[high], arr[p]
        else:
            p += 1
    return (low+1, p-1)

def insertion_sort(arr, i, j):
    for a in range(i+1, j+1):
        v = arr[a]
        b = a
        while b > i and arr[b-1] > v:
            arr[b] = arr[b-1]
            b -= 1
        arr[b] = v

def median_of_median(arr, i, j):
    n = j - i + 1
    _len = n // 5
    if n % 5 > 0:
        _len += 1
    medians = [0] * _len

    for a in range(i, j+1, 5):
        b = min(j, a + 4)
        insertion_sort(arr, a, b)
        if (b - a + 1) & 1 == 1:
            m = arr[(a+b)//2]
        else:
            m = arr[(a+b)//2+1]
        medians[(a-i)//5] = m

    mid = _len // 2 - 1
    return select(medians, 0, _len-1, mid)

def quick_sort(arr):
    do_quick_sort(arr, 0, len(arr)-1)

def do_quick_sort(arr, i, j):
    n = j - i + 1
    if n <= 5:
        insertion_sort(arr, i, j)
        return
    mid = median_of_median(arr, i, j)
    a, b = bi_partition(arr, i, j, mid)
    if i < a:
        do_quick_sort(arr, i, a-1)
    if b < j:
        do_quick_sort(arr, b+1, j)

def quick_sort2(arr):
    do_quick_sort2(arr, 0, len(arr)-1)

def do_quick_sort2(arr, i, j):
    n = j - i + 1
    if n <= 5:
        insertion_sort(arr, i, j)
        return

    pivot = median_of_3(arr, i, j)
    low = i
    high = j-1
    while True:
        low += 1
        while arr[low] < pivot:
            low += 1
        high -= 1
        while arr[high] > pivot:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    if low != high-1:
        arr[low], arr[j-1] = arr[j-1], arr[low]

    do_quick_sort2(arr, i, low-1)
    do_quick_sort2(arr, low+1, j)

def median_of_3(arr, i, j):
    c = (i+j) // 2
    if arr[i] > arr[c]:
        arr[i], arr[c] = arr[c], arr[i]
    if arr[c] > arr[j]:
        arr[j], arr[c] = arr[c], arr[j]
    if arr[i] > arr[c]:
        arr[i], arr[c] = arr[c], arr[i]

    # arr[i] <= arr[c] <= arr[j]

    arr[c], arr[j-1] = arr[j-1], arr[c]
    return arr[j-1]

@testwrapper
def test(arr, k):
    dup = arr[:]
    print(arr, k)
    print(kth_element(arr, k))
    print(arr)
    quick_sort2(dup)
    print(dup)

def main():
    test([9,4,1,2,3,8,5,6,7,0], 3)
    test([9,4,1,2,3,8,5,6,7,0], 0)
    test([9,4,1,2,3,8,5,6,7,0], 9)
    test([9,4,1,2,3,8,5,6,7,0], 1)
    test([9,4,1,2,3,8,5,6,7,0], 8)
    test([2,1,2,1,3,2,2,3,1,3,2,3,1,2], 3)
    test([2,1,2,1,3,2,2,3,1,3,2,3,1,2], 6)
    test([2,1,2,1,3,2,2,3,1,3,2,3,1,2], 10)
    test([13,81,92,43,31,65,57,26,75,0], 4)
    test([13,81,92,43,31,65,57,26,75,0], 0)
    test([13,81,92,43,31,65,57,26,75,0], 9)

if __name__ == '__main__':
    main()
