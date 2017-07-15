#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from graph import *

MAX = 0x7fffffff

def find_path(g, start, end):
    n = g.size()
    cost = [MAX] * n
    path = [-1] * n
    choose = [False] * n
    choose[start] = True

    p = g.first_adj(start)
    while p:
        cost[p.adj] = p.weight
        path[p.adj] = start
        p = p.next

    while True:
        i = find_min(cost, choose)
        if i == -1 or cost[i] == MAX:
            break
        choose[i] = True
        p = g.first_adj(i)
        while p:
            if not choose[p.adj] and (cost[p.adj] == MAX or cost[p.adj] < min(cost[i], p.weight)):
                cost[p.adj] = min(cost[i], p.weight)
                path[p.adj] = i
            p = p.next

    if path[end] == -1:
        return (0, None)

    seq = []
    i = end
    while i >= 0:
        seq.append(i)
        i = path[i]
    seq = seq[::-1]

    for j in range(0, len(seq)-1):
        subtract_edge(g, seq[j], seq[j+1], cost[end])
        add_edge(g, seq[j+1], seq[j], cost[end])

    return (cost[end], seq)

def find_min(cost, choose):
    i = -1
    c = MAX
    for j, w in enumerate(cost):
        if not choose[j] and w < c:
            c = w
            i = j
    return i

def subtract_edge(g, v, w, cost):
    p = g.first_adj(v)
    while p:
        if p.adj == w:
            if p.weight > cost:
                p.weight -= cost
            else:
                prv = p.prev
                nxt = p.next
                prv.next = nxt
                if nxt:
                    nxt.prev = prv
            break
        p = p.next

def show_max_stream(g, start, end):
    rsd = g.clone()
    mst = g.clone_without_edges()

    while True:
        weight, path = find_path(rsd, start, end)
        if not path:
            break
        merge_path(mst, path, weight)

    stream = 0
    p = mst.first_adj(start)
    while p:
        stream += p.weight
        p = p.next

    mst.dump()
    print('max stream:', stream)

def merge_path(g, path, cost):
    for i in range(0, len(path)-1):
        add_edge(g, path[i], path[i+1], cost)

def add_edge(g, v, w, cost):
    p = g.first_adj(v)
    while p:
        if p.adj == w:
            break
        p = p.next

    if not p:
        h = g.list[v]
        nxt = h.next
        p = AdjNode(w, 0)
        h.next = p
        p.prev = h
        if nxt:
            p.next = nxt
            nxt.prev = p

    p.weight += cost

def test(vex, edge, start_vex, end_vex):
    g = AdjList.parse(vex, edge)
    show_max_stream(g, g.vex_id(start_vex), g.vex_id(end_vex))

def main():
    '''网络流'''
    test(['s','a','c','b','d','t'],
            [('s','a',3),('s','b',2),
             ('a','b',1),('a','d',4),
             ('a','c',3),('b','d',2),
             ('c','t',2),('d','t',3)],
        's', 't')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
