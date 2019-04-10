#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

class Array:

    def __init__(self, arr):
        self.arr = arr
        self.p = len(arr) - 1

    def has_next(self):
        return self.p > 0

    def forward(self):
        self.p -= 1

    @property
    def value(self):
        return self.arr[self.p]

def top_k(arrs, k):
    n = len(arrs)
    heap = [None]
    for i in range(n):
        heap.append(Array(arrs[i]))
    heap_size = n

    for i in range(n//2, 0, -1):
        heapify(heap, heap_size, i)

    results = []
    for _ in range(k):
        results.append(heap[1].value)
        if heap[1].has_next():
            heap[1].forward()
        elif heap_size > 1:
            heap[1] = heap[heap_size]
            heap_size -= 1
        else:
            break
        heapify(heap, heap_size, 1)

    return results

def heapify(heap, size, i):
    while i <= size//2:
        L = i * 2
        R = L + 1
        if R <= size and heap[L].value < heap[R].value:
            k = R
        else:
            k = L
        if heap[k].value > heap[i].value:
            heap[i], heap[k] = heap[k], heap[i]
        i = k

@testwrapper
def test(arrs, k):
    print(arrs, k)
    print(top_k(arrs, k))

def main():
    test([[219,405,538,845,971],[148,558],[52,99,348,691]], 5)
    test([[219,405,538,845,971],[148,558],[52,99,348,691]], 11)
    test([[219,405,538,845,971],[148,558],[52,99,348,691]], 20)

if __name__ == '__main__':
    main()
