#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from graph import *

MAX = 0x7fffffff

def test(vex, edge, src):
    g = AdjList.parse(vex, edge)
    paths = dijkstra(g, g.vex_id(src))
    for p in paths:
        print(list(map(lambda x: g.vex_name(x), p)))
    print()

def dijkstra(g, start):
    n = g.size()
    dist = [MAX] * n
    path = [-1] * n

    p = g.first_adj(start)
    while p:
        dist[p.adj] = p.weight
        path[p.adj] = start
        p = p.next

    finished = set([start])
    while True:
        i = find_min(dist, finished)
        if i == -1 or dist[i] == MAX:
            break
        finished.add(i)
        p = g.first_adj(i)
        while p:
            if p.adj not in finished and dist[i] + p.weight < dist[p.adj]:
                dist[p.adj] = dist[i] + p.weight
                path[p.adj] = i
            p = p.next

    all_path = []
    for i in range(n):
        r = []
        p = i
        while p >= 0:
            r.append(p)
            p = path[p]
        if r[-1] == start:
            all_path.append(r[::-1])

    return all_path

def find_min(dist, finished):
    i = 0
    for j in range(1, len(dist)):
        if j not in finished and dist[j] < dist[i]:
            i = j
    return i if dist[i] < MAX else -1

def main():
    '''单源最短路径'''
    test([1,2,3,4,5,6,7], [(1,2,2),(1,4,1),(2,4,3),(2,5,10),(3,1,4),(3,6,5),
            (4,3,2),(4,5,2),(4,6,8),(4,7,4),(5,7,6),(7,6,1)], 1)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
