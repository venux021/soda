#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

class Node:

    def __init__(self, a1, i1, a2, i2):
        self.a1 = a1
        self.i1 = i1
        self.a2 = a2
        self.i2 = i2

    @property
    def value(self):
        return self.a1[self.i1] + self.a2[self.i2]

    def __lt__(self, n):
        return self.value < n.value

    def __eq__(self, n):
        return self.value == n.value

    def subseq(self):
        if self.i2 > 0:
            yield Node(self.a1, self.i1, self.a2, self.i2-1)
        if self.i1 > 0:
            yield Node(self.a1, self.i1-1, self.a2, self.i2)

    @property
    def location(self):
        return (self.i1, self.i2)

class Heap:

    def __init__(self):
        self.heap = [None]
        self.size = 0

    def top(self):
        return self.heap[1] if self.size > 0 else None

    def push(self, node):
        if self.size + 1 == len(self.heap):
            self.heap.append(node)
        else:
            self.heap[self.size+1] = node
        self.size += 1
        i = self.size
        while i > 1:
            parent = i // 2
            if self.heap[parent] < self.heap[i]:
                self.swap(parent, i)
                i = parent
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def pop(self):
        if self.size == 0:
            return
        res = self.top()
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        i = 1
        end = self.size // 2
        while i <= end:
            L = i * 2
            R = L + 1
            if R > self.size or self.heap[R] < self.heap[L]:
                T = L
            else:
                T = R
            if self.heap[i] < self.heap[T]:
                self.swap(i, T)
                i = T
            else:
                break
        return res

def sum_top_k(a1, a2, k):
    heap = Heap()
    node = Node(a1, len(a1)-1, a2, len(a2)-1)
    heap.push(node)
    n = 0
    buf = []
    locs = set()
    locs.add(node.location)
    while heap.size > 0 and n < k:
        t = heap.pop()
        buf.append(t.value)
        for p in t.subseq():
            if p.location not in locs:
                heap.push(p)
                locs.add(p.location)
        n += 1
    return buf

@testwrapper
def test(a1, a2, k):
    print(a1, a2, k)
    print(sum_top_k(a1, a2, k))

def main():
    test([1,2,3,4,5],[3,5,7,9,11], 4)
    test([1,2,3,4,5],[3,5,7,9,11], 26)

if __name__ == '__main__':
    main()
