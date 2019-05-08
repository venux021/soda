#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

class Heap:

    def __init__(self, *, key = None):
        self.heap = [None]
        self.size = 0
        if key:
            self.key_func = key
        else:
            self.key_func = lambda x: x

    def top(self):
        return self.heap[1] if self.size > 0 else None

    def pop(self):
        if self.size == 0:
            return
        res = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        i = 1
        half = self.size // 2
        while i <= half:
            L = i * 2
            R = L + 1
            if R > self.size or self.less_than(L, R):
                T = L
            else:
                T = R
            if self.less_than(T, i):
                self.swap(T, i)
                i = T
            else:
                break
        return res

    def less_than(self, i, j):
        return self.key_func(self.heap[i]) < self.key_func(self.heap[j])

    def push(self, v):
        if self.size + 1 == len(self.heap):
            self.heap.append(v)
        else:
            self.heap[self.size+1] = v
        self.size += 1
        i = self.size
        while i > 1:
            parent = i // 2
            if self.less_than(i, parent):
                self.swap(i, parent)
                i = parent
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

class MedianHolder:

    def __init__(self):
        self.min_heap = Heap()
        self.max_heap = Heap(key = lambda x: -x)
        self.size = 0

    def add(self, v):
        if self.size == 0:
            self.max_heap.push(v)
            self.size = 1
            return

        if v <= self.max_heap.top():
            self.max_heap.push(v)
        else:
            self.min_heap.push(v)

        if self.max_heap.size - self.min_heap.size == 2:
            t = self.max_heap.pop()
            self.min_heap.push(t)
        elif self.min_heap.size - self.max_heap.size == 2:
            t = self.min_heap.pop()
            self.max_heap.push(t)

        self.size += 1

    @property
    def median(self):
        if self.size == 0:
            return
        if self.size % 2 > 0:
            if self.min_heap.size > self.max_heap.size:
                return self.min_heap.top()
            else:
                return self.max_heap.top()
        else:
            return self.max_heap.top()

@testwrapper
def test(arr):
    mh = MedianHolder()
    for i in arr:
        mh.add(i)
        print(f'current: {i}, size: {mh.size}, median: {mh.median}')

def main():
    test([6,1,3,0,9,8,7,2])

if __name__ == '__main__':
    main()
