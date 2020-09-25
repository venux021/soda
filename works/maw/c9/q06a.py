#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from graph import *

def articulation_point(g):
    n = g.size()
    num = [0] * n
    low = [0] * n
    counter = [1]
    
    num[0] = 1
    p = g.first_adj(0)
    child = 0
    while p:
        if num[p.adj] == 0:
            dfs(g, p.adj, 0, num, low, counter)
            child += 1
        p = p.next

    if child > 1:
        print('articulation point: {}'.format(g.vex_name(0)))

def dfs(g, v, parent, num, low, counter):
    counter[0] += 1
    num[v] = counter[0]
    low[v] = num[v]

    p = g.first_adj(v)
    while p:
        w = p.adj
        if num[w] == 0:
            dfs(g, w, v, num, low, counter)
            if low[w] >= num[v]:
                print('articulation point: {}'.format(g.vex_name(v)))
            low[v] = min(low[v], low[w])
        elif w != parent:
            low[v] = min(low[v], num[w])
        p = p.next

def test(vs, edge):
    g = AdjList.parse_undirect(vs, edge)
    articulation_point(g)
    print('----')

def main():
    '''求割点'''
    test('D B C A E F G',
            [('A','B'),('A','D'),
             ('B','C'),('C','D'),
             ('C','G'),('D','E'),
             ('D','F'),('E','F')])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
