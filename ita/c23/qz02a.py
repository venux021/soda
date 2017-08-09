#!/usr/bin/env python3
import sys

from sodacomm.graph import *

MAX = sys.maxsize

class AgNode:

    def __init__(self, edge, weight):
        self.edge = edge
        self.weight = weight

class dsNode:

    def __init__(self):
        self.parent = -1
        self.rank = 1

class DSet:

    def __init__(self, size):
        self.arr = [dsNode() for i in range(size)]
        
    def merge(self, a, b):
        if self.arr[a].rank < self.arr[b].rank:
            t = a
            a = b
            b = t
        self.arr[b].parent = a
        self.arr[a].rank += self.arr[b].rank

    def find_parent(self, u):
        p = u
        while self.arr[u].parent >= 0:
            u = self.arr[u].parent
        while p != u:
            t = self.arr[p].parent
            self.arr[p].parent = u
            p = t
        return u

def mst_with_pre_proc(g):
    n = g.size()
    marks = [False] * n
    ds = DSet(n)
    T = []

    for i in range(n):
        if not marks[i]:
            mi_p = None
            for p in g.adj_of(i):
                if mi_p is None or p.weight < mi_p.weight:
                    mi_p = p
            v = mi_p.adj
            ds.merge(i, v)

            T.append((i, v))
            marks[i] = marks[v] = True

    amx = [[None] * n for i in range(n)]
    for i, j, w in g.iter_edges():
        u = ds.find_parent(i)
        v = ds.find_parent(j)
        if not amx[u][v]:
            amx[u][v] = AgNode((i,j), w)
        elif w < amx[u][v].weight:
            amx[u][v].edge = (i,j)
            amx[u][v].weight = w

    es = get_mst(amx) # TODO
    for e in es:
        ek = amx[e[0]][e[1]].edge
        print(g.vex_name(ek[0]), g.vex_name(ek[1]))
    for e in T:
        print(g.vex_name(e[0]), g.vex_name(e[1]))

class DistNode:

    def __init__(self, from_vex, to_vex, weight):
        self.from_vex = from_vex
        self.to_vex = to_vex
        self.weight = weight

def get_mst(amx):
    n = len(amx)
    i = 0
    while True:
        for j in range(n):
            if amx[i][j]:
                break
        i += 1

    visited = [False] * n
    dist = [None] * n
    for j in range(n):
        if amx[i][j]:
            dist[j] = DistNode(i,j,amx[i][j].weight)

    edges = []
    while True:
        s = select_min(dist)
        if s is None:
            break

        edges.append((dist[s].from_vex, dist[s].to_vex))
        dist[s] = None
        for j in range(n):
            if amx[s][j]:
                if not dist[j]: 
                    dist[j] = DistNode(s,j,amx[s][j].weight)
                elif dist[j].weight > amx[s][j].weight:
                    dist[j].weight = amx[s][j].weight
                    dist[j].from_vex = s

def select_min(dist):
    pass

def test(vex, edge):
    g = AdjList.parse_undirect(vex, edge)
    mst_with_pre_proc(g)

def main():
    '''稀疏图的最小生成树'''
    test('a b c d e f g h i',
            'a,b,4 a,h,8 b,c,8 b,h,11 c,d,7 c,f,4 c,i,2 d,e,9 d,f,14 e,f,10 f,g,2 g,i,6 g,h,1 h,i,7')

if __name__ == '__main__':
    main()
