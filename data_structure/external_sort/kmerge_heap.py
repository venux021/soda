#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

class DataSeq:

    def __init__(self, iterable):
        self.iter = iter(iterable)
        self.forward()

    def forward(self):
        try:
            self.cur = next(self.iter)
        except StopIteration:
            self.cur = sys.maxsize
        return self.cur

class MHeap:

    def __init__(self, *iterables):
        self.N = n = len(iterables)
        self.heap = [None] * (n+1)
        for i in range(n):
            self.heap[i+1] = DataSeq(iterables[i])
        self.initialize()

    def initialize(self):
        for i in range(self.N//2, 0, -1):
            self.adjust(i)

    def adjust(self, i):
        end = self.N // 2
        while i <= end:
            L = i * 2
            R = L + 1
            if R > self.N or self.heap[L].cur < self.heap[R].cur:
                T = L
            else:
                T = R
            if self.heap[i].cur > self.heap[T].cur:
                self.swap(i, T)
                i = T
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def pop(self):
        v = self.heap[1].cur
        self.heap[1].forward()
        self.adjust(1)
        return v

    def top(self):
        return self.heap[1].cur

@testwrapper
def test(*arrs):
    for a in arrs:
        print(a)
    mh = MHeap(*arrs)
    while True:
        v = mh.pop()
        if v == sys.maxsize:
            break
        print(v, end = ' ')
    print('')

def main():
    test([1,3,5,7,9], [2,4,9,13,24], [1,2,3,4,5,6,7,8,9,10], [-3,-2,-1,2,9,13], [-1,3,6,11,17,25,33,40])

if __name__ == '__main__':
    main()
