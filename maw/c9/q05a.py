#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from graph import *

MAX = 0x7fffffff

class PrimNode:
    def __init__(self):
        self.dist = MAX
        self.selected = False
        self.adj = -1

def show_minimal_tree(g):
    n = g.size()
    pm = [PrimNode() for i in range(n)]

    cost = 0
    pm[0].dist = 0
    while True:
        i = find_min(pm)
        if i == -1 or pm[i].dist == MAX:
            break
        cost += pm[i].dist
        if pm[i].adj != -1:
            print('({},{},{})'.format(g.vex_name(i), g.vex_name(pm[i].adj), pm[i].dist))
        pm[i].selected = True
        p = g.first_adj(i)
        while p:
            if not pm[p.adj].selected and p.weight < pm[p.adj].dist:
                pm[p.adj].dist = p.weight
                pm[p.adj].adj = i
            p = p.next

    print('cost:', cost)

def find_min(pm):
    i = -1
    c = MAX
    for j, v in enumerate(pm):
        if not v.selected and v.dist < c:
            c = v.dist
            i = j
    return i

def test(vex, edge):
    g = AdjList.parse_undirect(vex, edge)
    show_minimal_tree(g)

def main():
    '''Prim算法求最小生成树'''
    test([1,2,3,4,5,6,7],
            [(1,2,2),(1,3,4),(1,4,1),
             (2,4,3),(2,5,10),(3,4,2),
             (3,6,5),(4,5,7),(4,6,8),
             (4,7,4),(5,7,6),(6,7,1)])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
