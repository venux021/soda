#!/usr/bin/env python3
import sys

from sodacomm.graph import *

def find_path(g):
    n = g.size()
    visited = [[0] * n for i in range(n)]
    path = []

    dfs_path(g, 0, visited, path)

    print('path:', end = ' ')
    for p in path:
        print(g.vex_name(p), end = ' ')
    print()

def dfs_path(g, v, visited, path):
    path.append(v)
    for p in g.adj_of(v):
        if not visited[v][p.adj]:
            visited[v][p.adj] = visited[p.adj][v] = 1
            dfs_path(g, p.adj, visited, path)
            path.append(v)

def test(vex, edge):
    g = AdjList.parse_undirect(vex, edge)
    find_path(g)
    print('----')

def main():
    '''找出分别以正、反向通过每条边的路径'''
    test('a b c d e f',
            'a,b a,c b,d b,e c,e c,f e,f')
    test('e b c d a f',
            'a,b a,c b,d b,e c,e c,f e,f')

if __name__ == '__main__':
    main()
