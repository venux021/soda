#!/usr/bin/env python3
import sys

from sodacomm.graph import *

def show_scc(g):
    n = g.size()

    stk = []
    dfs_mark(g, stk)

    T = transposition(g)

    visited = [False] * n
    while stk:
        i = stk.pop()
        if visited[i]:
            continue
        vex = []
        dfs_scc(T, i, visited, vex)
        print('scc: {}'.format(','.join(list(map(lambda x: g.vex_name(x), vex)))))

def transposition(g):
    c = g.clone_without_edges()
    n = g.size()
    for i in range(n):
        for p in g.adj_of(i):
            c.add_edge(p.adj, i)
    return c

def dfs_scc(g, v, visited, vex):
    visited[v] = True
    vex.append(v)
    for p in g.adj_of(v):
        if not visited[p.adj]:
            dfs_scc(g, p.adj, visited, vex)

def dfs_mark(g, stk):
    n = g.size()
    visited = [False] * g.size()
    for i in range(n):
        if not visited[i]:
            _dfs_mark(g, stk, i, visited)

def _dfs_mark(g, stk, v, visited):
    visited[v] = True
    for p in g.adj_of(v):
        if not visited[p.adj]:
            _dfs_mark(g, stk, p.adj, visited)
    stk.append(v)

def test(vex, edge):
    g = AdjList.parse(vex, edge)
    show_scc(g)

def main():
    '''求强连通分量'''
    test('a b c d e f g h',
            'a,b b,c b,e b,f c,d c,g d,c d,h e,a e,f f,g g,f g,h h,h')
    test('A B C D E F G H I J',
            'A,C B,A C,F C,B D,A D,C E,D E,C F,B F,G F,H H,G H,I I,J J,H')

if __name__ == '__main__':
    main()
