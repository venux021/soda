#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('../..')

from maw.c9 import graph

MAX = sys.maxsize

def johnson(g):
    n = g.size()
    
    s = g.add_vex('s')
    for i in range(n):
        g.add_edge(s, i, 0)

    dist = bellman_ford(g, s)
    if not dist:
        return

    for i in range(g.size()):
        for p in g.adj_of(i):
            p.weight = p.weight + dist[i] - dist[p.adj]

    for i in range(n):
        D = [0] * n
        P = [-1] * n
        dijkstra(g, i, D, P)
        for j in range(len(D)):
            if i != j and D[j] < MAX:
                D[j] = D[j] + dist[j] - dist[i]

        show_path(g, i, D, P)

def show_path(g, s, D, P):
    n = g.size() - 1  # exclude the last vex
    for i in range(n):
        if i == s:
            continue
        path = []
        j = i
        while j >= 0:
            path.append(j)
            j = P[j]
        if len(path) > 1:
            path = path[::-1]
            print('[{:3d}] {}'.format(D[i], ' -> '.join(map(lambda x: g.vex_name(x), path))))

def dijkstra(g, s, D, P):
    n = g.size() - 1  # exclude the last vex 
    h = DijkHeap(n)

    h.update(s, s, 0)

    while not h.empty():
        t = h.pop()
        if t.dist == MAX:
            break
        D[t.to] = t.dist
        if t.frm != t.to:
            P[t.to] = t.frm
        for p in g.adj_of(t.to):
            h.update(t.to, p.adj, t.dist + p.weight)

class HNode:

    def __init__(self, frm, to, dist):
        self.index = -1
        self.frm = frm
        self.to = to
        self.dist = dist

class DijkHeap:

    def __init__(self, n):
        self.nodes = [HNode(-1,-1,MAX) for i in range(n)]
        self.h = [None] * (n+1)
        for i in range(n):
            self.h[i+1] = self.nodes[i]
            self.nodes[i].index = i+1
            self.nodes[i].to = i
        self.size = n

    def dump(self):
        for i in range(self.size):
            print(self.h[i+1].dist, end = ' ')
        print()

    def empty(self):
        return self.size == 0

    def update(self, frm, to, new_dist):
        if self.nodes[to].dist > new_dist:
            self.nodes[to].dist = new_dist
            self.nodes[to].frm = frm
            self.adjust_up(self.nodes[to].index)

    def adjust_up(self, s):
        while s > 1:
            p = s >> 1
            if self.h[s].dist < self.h[p].dist:
                pn = self.h[p]
                sn = self.h[s]
                pn.index = s
                sn.index = p
                t = self.h[s]
                self.h[s] = self.h[p]
                self.h[p] = t
                s = p
            else:
                break

    def pop(self):
        if self.empty():
            return

        t = self.h[1]
        self.h[1] = self.h[self.size]
        self.h[1].index = 1
        self.size -= 1
        self.adjust_down(1)
        return t

    def adjust_down(self, s):
        while True:
            L = s * 2
            R = L + 1
            if L > self.size:
                break
            elif L == self.size:
                child = L
            elif self.h[L].dist < self.h[R].dist:
                child = L
            else:
                child = R

            if self.h[s].dist > self.h[child].dist:
                sn = self.h[s]
                cn = self.h[child]
                sn.index = child
                cn.index = s
                t = self.h[s]
                self.h[s] = self.h[child]
                self.h[child] = t
                s = child
            else:
                break

def bellman_ford(g, s):
    n = g.size()
    dist = [MAX] * n
    dist[s] = 0

    for p in g.adj_of(s):
        dist[p.adj] = p.weight

    for i in range(n-1):
        for x, y, w in g.iter_edges():
            if dist[x] < MAX and dist[x] + w < dist[y]:
                dist[y] = dist[x] + w

    for x, y, w in g.iter_edges():
        if dist[y] > dist[x] + w:
            print('negative circuit')
            return

    return dist

def test(vex, edge):
    g = graph.AdjList.parse(vex, edge)
    johnson(g)

def main():
    '''用于稀疏图的Johnson算法计算每对点之最短路径'''
    test('1 2 3 4 5', [('1','2',3),('1','3',8),('1','5',-4),
            ('2','4',1),('2','5',7),('3','2',4),('4','1',2),
            ('4','3',-5),('5','4',6)])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
