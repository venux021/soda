#!/usr/bin/env python3
import sys

from sodacomm.graph import *

MAX = sys.maxsize

def mst_with_pre_proc(g):
    n = g.size()
    marks = [False] * n
    ds = DSet(n) # TODO
    T = []

    for i in range(n):
        if not marks[i]:
            mi_p = None
            for p in g.adj_of(i):
                if mi_p is None or p.weight < mi_p.weight:
                    mi_p = p
            v = mi_p.adj
            ds.merge(i, v)  # TODO

            T.append((i, v))
            marks[i] = marks[v] = True

    amx = [[None] * n for i in range(n)]
    for i, j, w in g.iter_edges():
        u = ds.find_parent()

def test(vex, edge):
    g = AdjList.parse_undirect(vex, edge)
    mst_with_pre_proc(g)

def main():
    '''稀疏图的最小生成树'''
    test('a b c d e f g h i',
            'a,b,4 a,h,8 b,c,8 b,h,11 c,d,7 c,f,4 c,i,2 d,e,9 d,f,14 e,f,10 f,g,2 g,i,6 g,h,1 h,i,7')

if __name__ == '__main__':
    main()
