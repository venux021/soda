#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('../..')

from maw.c9 import graph

class VNode:

    def __init__(self, vex):
        self.u = vex
        self.next = self.prev = None
        self.current = None

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

    adj_list = [graph.AdjNode(-1) for i in range(n)]

    head = tail = VNode(-1)
    for i in range(n):
        for p in g.adj_of(i):
            n1 = graph.AdjNode(p.adj)
            insert_head(adj_list, i, n1)
            n2 = graph.AdjNode(i)
            insert_head(adj_list, p.adj, n2)
        
        if i != s and i != t:
            vn = VNode(i)
            vn.current = adj_list[i].next
            tail.next = vn
            vn.prev = tail
            tail = vn

    p = head.next
    while p:
        old_h = h[p.u]

        while e[p.u] > 0:
            v = p.current
            if not v:
                min_h = sys.maxsize
                for j in range(n):
                    if res[p.u][j] > 0:
                        min_h = min(min_h, h[j])
                h[p.u] = min_h + 1
                p.current = adj_list[p.u].next
            elif res[p.u][v.adj] > 0 and h[p.u] - h[v.adj] == 1:
                k = min(e[p.u], res[p.u][v.adj])
                if E[p.u][v.adj]:
                    F[p.u][v.adj] += k
                else:
                    F[v.adj][p.u] -= k
                e[p.u] -= k
                e[v.adj] += k
                res[p.u][v.adj] -= k
                res[v.adj][p.u] += k
            else:
                p.current = v.next

        if h[p.u] > old_h:
            if p != head.next:
                prv = p.prev
                nxt = p.next
                prv.next = nxt
                if nxt:
                    nxt.prev = prv
                first = head.next
                p.next = first
                first.prev = p
                head.next = p
                p.prev = head

        p = p.next

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


def insert_head(adj_list, k, node):
    nxt = adj_list[k].next
    node.next = nxt
    if nxt:
        nxt.prev = node
    adj_list[k].next = node
    node.prev = adj_list[k]

def test(vex, edge, start, end):
    g = graph.AdjList.parse(vex, edge)
    max_flow(g, g.vex_id(start), g.vex_id(end))
    print('------')

def main():
    '''前置重贴标签法求最大流'''
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
