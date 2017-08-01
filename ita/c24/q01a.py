#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('../..')

MAX = sys.maxsize

from maw.c9 import graph

def bellman_ford(g, s):
    n = g.size()
    dist = [MAX] * n
    dist[s] = 0
    prev = [-1] * n

    for p in g.adj_of(s):
        dist[p.adj] = p.weight
        prev[p.adj] = s

    for i in range(n-1):
        for x, y, w in g.iter_edges():
            k = dist[x] + w
            if dist[y] > k:
                dist[y] = k
                prev[y] = x

    for x, y, w in g.iter_edges():
        if dist[y] > dist[x] + w:
            print('negative weight circuit')
            return

    for i in range(n):
        if i == s:
            continue
        path = []
        p = i
        while p >= 0:
            path.append(g.vex_name(p))
            p = prev[p]
        print('{}, {} -> {}: {}'.format(dist[i], g.vex_name(s), g.vex_name(i), path[::-1]))

def test(vex, edge, start):
    g = graph.AdjList.parse(vex, edge)
    bellman_ford(g, g.vex_id(start))

def main():
    '''Bellman-Ford求解单源最短路径'''
    test('s t x y z', [('s','t',6),('s','y',7),('t','x',5),
                   ('t','y',8),('t','z',-4),('x','t',-2),
                   ('y','x',-3),('y','z',9),('z','x',7),('z','s',2)],
                   's')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
