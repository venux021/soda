#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from collections import deque
sys.path.append('../..')

from maw.c9 import graph

MAX = 0x7fffffff
MIN = -MAX

def max_flow(g, s, t):
    n = g.size()

    edge = [[False] * n for i in range(n)]
    res = [[0] * n for i in range(n)]
    f = [[0] * n for i in range(n)]

    for i, j, w in g.iter_edges():
        edge[i][j] = True
        res[i][j] = w

    while True:
#        flow, path = dfs_path(res, s, t)
        flow, path = breadth_first_path(res, s, t)
        if flow == 0:
            break

        for p in path:
            a, b = p
            if edge[a][b]:
                f[a][b] += flow
            else:
                f[b][a] -= flow
            res[a][b] -= flow
            res[b][a] += flow

    cg = g.clone_without_edges()
    for i in range(n):
        for j in range(n):
            if f[i][j] > 0:
                cg.add_edge(i, j, f[i][j])

    cg.dump()
    mf = 0
    for p in cg.adj_of(s):
        mf += p.weight
    print('max flow:', mf)

def breadth_first_path(res, s, t):
    n = len(res)
    q = deque()

    visited = [False] * n
    prev = [-1] * n

    q.append(s)
    while q:
        i = q.popleft()
        visited[i] = True
        reach_end = False
        for j in range(n):
            if res[i][j] > 0 and not visited[j]:
                prev[j] = i
                if j == t:
                    reach_end = True
                    break
                q.append(j)
        if reach_end:
            break
    else:
        return (0, [])

    seq = []
    i = t
    while i >= 0:
        seq.append(i)
        i = prev[i]

    seq = seq[::-1]

    path = []
    flow = MAX
    for i in range(len(seq)-1):
        path.append((seq[i], seq[i+1]))
        flow = min(flow, res[seq[i]][seq[i+1]])

    return (flow, path)

def dfs_path(res, s, t):
    ps = []
    visited = [False] * len(res)
    if _dfs(res, s, t, ps, visited):
        flow = MAX
        path = []
        for i in range(len(ps)-1):
            flow = min(flow, res[ps[i]][ps[i+1]])
            path.append((ps[i], ps[i+1]))
        return (flow, path)
    else:
        return (0, [])

def _dfs(res, v, t, ps, visited):
    ps.append(v)
    visited[v] = True

    if v == t:
        return True

    for i in range(len(res)):
        if not visited[i] and res[v][i] != 0 and _dfs(res, i, t, ps, visited):
            return True

    ps.pop()
    return False

def test(vex, edge, start, end):
    g = graph.AdjList.parse(vex, edge)
    max_flow(g, g.vex_id(start), g.vex_id(end))
    print('------')

def main():
    '''最大流'''
    test('s 1 2 3 4 t', [('s','1',16),('s','2',13),
                         ('1','3',12),('2','1',4),
                         ('2','4',14),('3','2',9),
                         ('3','t',20),('4','3',7),
                         ('4','t',4)],
        's', 't')

    test('s a b c d t', [('s','a',3),('s','b',2),
            ('a','c',3),('a','d',4),('a','b',1),
            ('b','d',2),('c','t',2),('d','t',3)],
        's', 't')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
