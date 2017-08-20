#!/usr/bin/env python3
import sys
from collections import deque

from sodacomm.graph import *

def get_diameter(g):
    n = g.size()
    q = deque()
    q.append(0)
    L = [-1] * n
    max_v = 0
    L[0] = 0

    while q:
        t = q.popleft()
        for p in g.adj_of(t):
            if L[p.adj] == -1:
                q.append(p.adj)
                L[p.adj] = L[t] + 1
                if L[max_v] < L[p.adj]:
                    max_v = p.adj

    L = [-1] * n
    q.append(max_v)
    L[max_v] = 0
    max_L = 0
    while q:
        t = q.popleft()
        for p in g.adj_of(t):
            if L[p.adj] == -1:
                q.append(p.adj)
                L[p.adj] = L[t] + 1
                max_L = max(max_L, L[p.adj])

    return max_L

def test(vex, edge):
    g = AdjList.parse_undirect(vex, edge)
    print('diameter:', get_diameter(g))

def main():
    '''求树的直径'''
    test('c b d e f a',
            'a,b a,c b,d c,e c,f')
    test('c b d e f a',
            'a,b a,c b,d f,e c,f')

if __name__ == '__main__':
    main()
