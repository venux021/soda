#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

class Node1:

    def __init__(self, s, c):
        self.s = s
        self.c = c

class MinHeap1:

    def __init__(self, capacity):
        self.heap = [None] * (capacity + 1)
        self.size = 0

    @property
    def capacity(self):
        return len(self.heap) - 1

    def top(self):
        return self.heap[1] if self.size > 0 else None

    def push(self, node):
        if self.size == self.capacity:
            if node.c > self.top().c:
                self.heap[1] = node
                self.heapify_desc(1)
        else:
            self.size += 1
            self.heap[self.size] = node
            self.heapify_asc(self.size)

    def pop(self):
        if self.size == 0:
            return
        res = self.top()
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heapify_desc(1)
        return res

    def heapify_desc(self, i):
        end = self.size // 2
        while i <= end:
            L = i * 2
            R = L + 1
            if R > self.size or self.heap[L].c < self.heap[R].c:
                T = L
            else:
                T = R
            if self.heap[i].c > self.heap[T].c:
                self.swap(i, T)
                i = T
            else:
                break

    def heapify_asc(self, i):
        while i > 1:
            parent = i // 2
            if self.heap[i].c < self.heap[parent].c:
                i = parent
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

def times_top_k(ss, k):
    wc = {}
    for s in ss:
        wc[s] = wc.get(s,0) + 1
    mh = MinHeap1(k)
    for w, c in wc.items():
        mh.push(Node1(w,c))
    buf = []
    while mh.size:
        t = mh.pop()
        buf.append((t.s, t.c))
    return buf

class Node2:

    def __init__(self, word, count, index = -1):
        self.word = word
        self.count = count
        self.index = index

class TopKRecord:

    def __init__(self, k):
        self.k = k
        self.size = 0
        self.heap = [None] * (k+1)
        self.wc = {}

    def add(self, word):
        if word not in self.wc:
            node = self.wc[word] = Node2(word, 1)
            if self.size < self.k:
                self.push_heap(node)
        else:
            node = self.wc[word]
            node.count += 1
            if node.index == -1 and node.count > self.top().count:
                top = self.top()
                top.index = -1
                self.heap[1] = node
                node.index = 1
                self.heapify_desc(1)
            elif node.index > 0:
                self.heapify_desc(node.index)

    def push_heap(self, node):
        self.size += 1
        self.heap[self.size] = node
        node.index = self.size
        self.heapify_asc(self.size)

    def top(self):
        return self.heap[1]

    def heapify_desc(self, i):
        end = self.size // 2
        while i <= end:
            L = i * 2
            R = L + 1
            if R > self.size or self.heap[L].count < self.heap[R].count:
                T = L
            else:
                T = R
            if self.heap[i].count > self.heap[T].count:
                self.swap(i, T)
                i = T
            else:
                break

    def swap(self, i, j):
        ni = self.heap[i]
        nj = self.heap[j]
        self.heap[i] = nj
        nj.index = i
        self.heap[j] = ni
        ni.index = j

    def heapify_asc(self, i):
        while i > 1:
            parent = i // 2
            if self.heap[i].count < self.heap[parent].count:
                self.swap(i, parent)
                i = parent
            else:
                break

    def printTopK(self):
        for i in range(self.size):
            node = self.heap[i+1]
            print(node.word, node.count, end = ', ')
        print('')

@testwrapper
def test2():
    rec = TopKRecord(2)
    rec.add('A')
    rec.printTopK()
    rec.add('B')
    rec.add('B')
    rec.printTopK()
    rec.add('C')
    rec.add('C')
    rec.printTopK()
    rec.add('D')
    rec.add('D')
    rec.add('D')
    rec.printTopK()
    rec.add('A')
    rec.add('A')
    rec.add('A')
    rec.add('A')
    rec.printTopK()
    rec.add('C')
    rec.add('C')
    rec.add('C')
    rec.printTopK()

@testwrapper
def test1(ss, k):
    print(ss, k)
    res = times_top_k(ss, k)
    print(res)

def main():
    test1(['1','2','3','4'], 2)
    test1(['1','2','3','4'], 1)
    test1(['1','1','2','3'], 2)
    test1(['1','1','2','3'], 1)
    test2()

if __name__ == '__main__':
    main()
