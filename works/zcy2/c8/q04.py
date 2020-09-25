#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def find_mink(arr, k):
    heap = [0] * (k+1)
    n = len(arr)
    if n <= k:
        return arr
    heap[1:] = arr[:k]
    make_heap(heap)

    for c in arr[k:]:
        if c < heap[1]:
            heap[1] = c
            adjust_heap(heap, 1)
    return heap[1:]

def make_heap(heap):
    size = len(heap) - 1
    for i in range(size//2, 0, -1):
        adjust_heap(heap, i)

def adjust_heap(heap, i):
    size = len(heap) - 1
    while i <= size//2:
        L = i * 2
        R = L + 1
        if R <= size and heap[R] > heap[L]:
            heap[i], heap[R] = heap[R], heap[i]
            i = R
        else:
            heap[i], heap[L] = heap[L], heap[i]
            i = L

def kth_element(arr, k):
    n = len(arr)
    if k > n:
        return
    return select(arr, 0, n - 1, k - 1)

def select(arr, begin, end, t):
    median = []
    for i in range(begin, end+1, 5):
        j = min(end, i + 4)
        insertion_sort(arr, i, j)
        if j - i == 4:
            median.append(arr[i+2])
        elif (i+j) % 2 == 0:
            median.append(arr[(i+j)//2])
        else:
            median.append(arr[(i+j)//2+1])
    Mn = len(median)
    if Mn == 1:
        mm = median[0]
    else:
        mm = select(median, 0, len(median)-1, len(median)//2)

    i = partition(arr, begin, end, mm)
    if i == t:
        return arr[i]
    elif t < i:
        return select(arr, begin, i-1, t)
    else:
        return select(arr, i+1, end, t)

def insertion_sort(arr, i, j):
    for p in range(i+1, j+1):
        tmp = arr[p]
        k = p - 1
        while k >= i and arr[k] > arr[p]:
            arr[k+1] = arr[k]
            k -= 1
        arr[k+1] = tmp

def partition(arr, begin, end, v):
    small = begin - 1
    big = end + 1
    cur = begin
    while cur != big:
        if arr[cur] < v:
            small += 1
            swap(arr, small, cur)
            cur += 1
        elif arr[cur] > v:
            big -= 1
            swap(arr, cur, big)
        else:
            cur += 1
    return cur - 1

def swap(arr, i, j):
    if i != j:
        arr[i], arr[j] = arr[j], arr[i]

@testwrapper
def test(arr, k):
    print(arr, k)
    print(find_mink(arr, k))
    print(kth_element(arr, k))

def main():
    test([3,5,2,1,7,6,8,9], 4)
    test([3,5,2], 4)
    test([4,5,6,7,8,9,10,1,2,3,-1,0], 5)

if __name__ == '__main__':
    main()
