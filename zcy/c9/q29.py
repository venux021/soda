#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def top_k(arr, k):
    word_freq = {}
    max_freq = 0
    for w in arr:
        word_freq[w] = word_freq.get(w, 0) + 1
        max_freq = max(word_freq[w], max_freq)

    freqs = [None] * (max_freq + 1)

    for w, fr in word_freq.items():
        if freqs[fr] is None:
            freqs[fr] = []
        freqs[fr].append(w)

    c = 0
    r = []
    for i in range(max_freq, 0, -1):
        if not freqs[i]:
            continue
        for w in freqs[i]:
            if c == k:
                break
            r.append((w, i))
            c += 1

    return r
        

def test(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    print 'top k: {}'.format(top_k(arr, k))

def test2(arr, k):
    print 'arr: {}, k: {}'.format(arr, k)
    top_k2(arr, k)

def top_k2(arr, k):
    tr = TopKRec(k)
    for w in arr:
        tr.add(w)
        tr.dump()

class Rec(object):

    def __init__(self, word):
        self.word = word
        self.index = -1
        self.count = 0

class TopKRec(object):

    def __init__(self, k):
        self.k = k
        self.wmap = {}
        self.heap = [None] * (k+1)
        self.heap_size = 0

    def push_heap(self, r):
        self.heap_size += 1
        i = self.heap_size
        self.heap[i] = r
        r.index = i
        H = self.heap
        while i > 1:
            p = i / 2
            if H[i].count < H[p].count:
                self._swap_node(i, p)
                i = p
            else:
                break

    def _swap_node(self, i, j):
        if i == j:
            return
        H = self.heap
        H[i].index = j
        H[j].index = i
        t = H[i]
        H[i] = H[j]
        H[j] = t

    def adjust_heap(self, index):
        i = index
        while True:
            lc = i * 2
            rc = lc + 1
            if lc > self.heap_size:
                break
            elif lc == self.heap_size:
                child = lc
            else:
                if self.heap[lc].count < self.heap[rc].count:
                    child = lc
                else:
                    child = rc
            if self.heap[i].count > self.heap[child].count:
                self._swap_node(i, child)
                i = child
            else:
                break

    def add(self, word):
        if word not in self.wmap:
            self.wmap[word] = Rec(word)
        r = self.wmap[word]
        r.count += 1
        if r.index < 0:
            if self.heap_size < self.k:
                self.push_heap(r)
            elif self.heap[1].count < r.count:
                self.heap[1].index = -1
                self.heap[1] = r
                r.index = 1
                self.adjust_heap(1)
        else:
            self.adjust_heap(r.index)

    def dump(self):
        for i in range(self.heap_size):
            r = self.heap[i+1]
            print r.word, r.count
        print '----'

def main():
    '''出现次数的TOP K 问题'''
    test(['1','2','3','4'], 2)
    test(['1','1','2','3'], 2)
    test(['1','1','2','3'], 3)
    test(['1','1','2','3'], 4)
    test(['1','1','2','3'], 5)
    test(['A', 'B', 'C', 'D', 'A', 'C', 'B', 'A'], 3)
    test2(['A','B','B','C','C'], 2)
    test2(['A', 'B', 'C', 'D', 'A', 'C', 'B', 'A'], 3)
    test2(['A', 'B', 'C', 'D', 'A', 'C', 'B', 'A', 'D', 'D', 'D'], 3)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
