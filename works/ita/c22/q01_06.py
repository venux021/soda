#!/usr/bin/env python3
import sys

from sodacomm.graph import *

def get_universal_sink(g):
    n = g.size()
    mx = g.adj_matrix()
    i = j = 0
    while i < n and j < n:
        if mx[i][j]:
            i += 1
        else:
            j += 1
    if i < n and is_universal_sink(mx, i):
        return i
    else:
        return -1

def is_universal_sink(mx, v):
    n = len(mx)
    for j in range(n):
        if mx[v][j]:
            return False
    for i in range(n):
        if not mx[i][v] and i != v:
            return False
    return True

def test(vex, edge):
    g = AdjList.parse(vex, edge)
    us = get_universal_sink(g)
    if us >= 0:
        print('universal sink is', g.vex_name(us))
    else: 
        print('No universal sink')

def main():
    '''判断有向图是否存在通用汇点'''
    test('a b c d',
            'a,b a,d a,c b,c d,c')
    test('a b c d e',
            'a,c b,a b,c b,e d,a e,d')

if __name__ == '__main__':
    main()
