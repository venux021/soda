#!/usr/bin/env python3
import sys
from collections import deque

from sodacomm.graph import *

def show_partition(g):
    n = g.size()
    role = [0] * n
    q = deque()
    q.append(0)

    role[0] = 1
    while q:
        t = q.popleft()
        for p in g.adj_of(t):
            if role[p.adj] == 0:
                role[p.adj] = 2 if role[t] == 1 else 1
                q.append(p.adj)
            elif role[p.adj] == role[t]:
                print('unable to partition')
                return

    for i, r in enumerate(role):
        if r == 1:
            print(g.vex_name(i), end = ' ')
    print()
    for i, r in enumerate(role):
        if r == 2:
            print(g.vex_name(i), end = ' ')
    print()

def test(vex, edge):
    g = AdjList.parse_undirect(vex, edge)
    show_partition(g)
    print('--------')

def main():
    '''摔跤手划分'''
    test('b c d e f a',
            'a,b a,c b,d c,e c,f')
    test('b c d e f a',
            'a,b a,c b,d c,e c,f b,e')
    test('b c d e f a',
            'a,b a,c b,d c,e c,f e,f')

if __name__ == '__main__':
    main()
