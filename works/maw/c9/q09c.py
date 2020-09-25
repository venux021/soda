#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from graph import *

def show_strong_conn(g, start):
    n = g.size()
    num = [-1] * n
    visited = [False] * n
    count = [0]
    def dfs_num(v):
        visited[v] = True
        p = g.first_adj(v)
        while p:
            if not visited[p.adj]:
                dfs_num(p.adj)
            p = p.next
        count[0] += 1
        num[v] = count[0]

    dfs_num(start)
    print(num)

    g2 = g.clone_without_edges()
    for i in range(n):
        p = g.first_adj(i)
        while p:
            g2.add_edge(p.adj, i, p.weight)
            p = p.next

    n2v = [-1] * (n+1)
    for i, no in enumerate(num):
        n2v[no] = i

    visited = [False] * n
    for i in range(n, 0, -1):
        v = n2v[i]
        if not visited[v]:
            vexes = []
            rev_dfs(g2, v, visited, vexes)
            print(list(map(lambda x: g.vex_name(x), vexes)))

def rev_dfs(g, v, visited, vexes):
    vexes.append(v)
    visited[v] = True
    p = g.first_adj(v)
    while p:
        if not visited[p.adj]:
            rev_dfs(g, p.adj, visited, vexes)
        p = p.next

def test(v, e, start):
    g = AdjList.parse(v, e)
    show_strong_conn(g, g.vex_id(start))

def main():
    '''查找强连通分支'''
    test('A B C D E F G H I J',
            'A,B;A,D;B,C;B,F;C,A;C,D;C,E;D,E;F,C;G,F;G,H;H,J;H,F;I,H;J,I',
            'G')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
