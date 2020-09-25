#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('../..')

from maw.c9 import graph

def max_flow(g, s, t):
    n = g.size()

    F = [[0] * n for i in range(n)]
    E = [[False] * n for i in range(n)]
    res = [[0] * n for i in range(n)]
    h = [0] * n
    e = [0] * n

    for i, j, w in g.iter_edges():
        res[i][j] = w
        E[i][j] = True

    h[s] = n
    for p in g.adj_of(s):
        res[s][p.adj] = 0
        res[p.adj][s] = F[s][p.adj] = p.weight
        e[p.adj] = p.weight
        e[s] -= p.weight

    vex = []
    for i in range(n):
        if i != s and i != t:
            vex.append(i)

    while True:
        push = False
        relabel = False
        for i in vex:
            has_pushed = False
            for j in range(n):
                if res[i][j] > 0 and e[i] > 0 and h[i] - h[j] == 1:
                    k = min(e[i], res[i][j])
                    if E[i][j]:
                        F[i][j] += k
                    else:
                        F[j][i] -= k
                    e[i] -= k
                    e[j] += k
                    res[i][j] -= k
                    res[j][i] += k
                    has_pushed = True

            if has_pushed:
                push = True
                continue

            need_relabel = False
            for j in range(n):
                if res[i][j] > 0 and e[i] > 0 and h[i] <= h[j]:
                    need_relabel = True
                    break

            if need_relabel:
                min_h = sys.maxsize
                for j in range(n):
                    if res[i][j] > 0:
                        min_h = min(min_h, h[j])
                h[i] = min_h + 1
                relabel = True

        if not push and not relabel:
            break

    cg = g.clone_without_edges()
    for i in range(n):
        for j in range(n):
            if F[i][j] > 0:
                cg.add_edge(i, j, F[i][j])

    cg.dump()
    mf = 0
    for p in cg.adj_of(s):
        mf += p.weight
    print('max flow:', mf)

def test(vex, edge, start, end):
    g = graph.AdjList.parse(vex, edge)
    max_flow(g, g.vex_id(start), g.vex_id(end))
    print('------')

def main():
    '''推送-重贴标签法求最大流'''
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
