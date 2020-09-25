#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from graph import *

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

class EdgeHeap:
    def __init__(self, n):
        self.h = [None] * (n+1)
        self.capacity = n
        self.size = 0
    def push(self, e):
        if self.size == self.capacity:
            return
        self.size += 1
        self.h[self.size] = e
        i = self.size
        while i > 1:
            p = i // 2
            if self.h[p].weight > self.h[i].weight:
                t = self.h[p]
                self.h[p] = self.h[i]
                self.h[i] = t
                i = p
            else:
                break

    def pop(self):
        if self.size == 0:
            return None

        r = self.h[1]
        self.h[1] = self.h[self.size]
        self.size -= 1
        i = 1
        while True:
            L = i * 2
            R = L + 1
            if L > self.size:
                break
            elif R > self.size:
                child = L
            else:
                child = L if self.h[L].weight < self.h[R].weight else R
            if self.h[child].weight < self.h[i].weight:
                t = self.h[child]
                self.h[child] = self.h[i]
                self.h[i] = t
                i = child
            else:
                break
        return r

def kruskal_minimal_tree(g):
    n = g.size()
    dj = DisjoinSet(n)

    es = []
    for i in range(n):
        p = g.first_adj(i)
        while p:
            if p.adj > i:
                es.append(Edge(i, p.adj, p.weight))
            p = p.next

    heap = EdgeHeap(len(es))
    for e in es:
        heap.push(e)

    cost = 0
    k = 0
    while k < n-1:
        e = heap.pop()
        if e is None:
            break
        v1, v2 = e.v, e.w
        p1 = dj.parent(v1)
        p2 = dj.parent(v2)
        if p1 == p2:
            continue

        cost += e.weight
        print('({},{},{})'.format(g.vex_name(v1), g.vex_name(v2), e.weight))

        dj.merge(p1, p2)
        k += 1

    print('cost:', cost)

class DisjoinSet:

    def __init__(self, size):
        self.arr = [-1] * size

    def parent(self, i):
        p = i
        while self.arr[p] >= 0:
            p = self.arr[p]
        t = i
        while t != p:
            k = t
            t = self.arr[t]
            self.arr[k] = p
        return p

    def merge(self, i, j):
        if self.arr[i] >= 0:
            i = parent(i)
        if self.arr[j] >= 0:
            j = parent(j)
        if self.arr[i] > self.arr[j]:
            self.arr[i] = j
        else:
            self.arr[j] = i

def test(vex, edge):
    g = AdjList.parse_undirect(vex, edge)
    kruskal_minimal_tree(g)

def main():
    '''Kruskal算法求最小生成树'''
    test([1,2,3,4,5,6,7],
            [(1,2,2),(1,3,4),(1,4,1),
             (2,4,3),(2,5,10),(3,4,2),
             (3,6,5),(4,5,7),(4,6,8),
             (4,7,4),(5,7,6),(6,7,1)])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
