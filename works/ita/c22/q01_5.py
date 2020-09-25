#!/usr/bin/env python3
import sys

from sodacomm.graph import *

def square_graph(g):
    n = g.size()
    amx = g.adj_matrix()
    g2 = g.clone_without_edges()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if amx[i][j] or amx[i][k] and amx[k][j]:
                    g2.add_edge(i,j)
                    break
    return g2

def test(vex, edge):
    g = AdjList.parse(vex, edge)
    g2 = square_graph(g)
    g2.dump()

def main():
    '''求平方图'''
    test('1 2 3 4 5 6',
            '1,2 1,4 2,5 3,5 3,6 4,2 5,4')

if __name__ == '__main__':
    main()
