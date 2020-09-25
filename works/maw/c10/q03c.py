#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('../..')

from maw.c9.graph import *

MAX = 0x2fffffff

def floyd(g):
    n = g.size()
    dp = [[MAX] * n for i in range(n)]
    path = [[-1] * n for i in range(n)]

    for i in range(n):
        p = g.first_adj(i)
        while p:
            dp[i][p.adj] = p.weight
            path[i][p.adj] = i
            p = p.next

    for k in range(n):
        for i in range(n):
            for j in range(n):
                z = dp[i][k] + dp[k][j]
                if z < dp[i][j]:
                    dp[i][j] = z
                    path[i][j] = path[k][j]

    for k in range(0, n):
        for i in range(0, n):
            if i == k or dp[k][i] == MAX:
                continue
            j = i
            step = []
            while j != k:
                step.append(g.vex_name(j))
                j = path[k][j]
            step.append(g.vex_name(k))
            print('{} -> {}'.format(step[-1], step[0]), 
                    '[{}]'.format(dp[k][i]), 
                    ','.join([str(x) for x in step[::-1]]))

def test(vex, edge):
    g = AdjList.parse(vex, edge)
    floyd(g)

def main():
    '''Floyd算法'''
    test([1,2,3,4,5,6,7], [(1,2,2),(1,4,1),(2,4,3),(2,5,10),(3,1,4),(3,6,5),
            (4,3,2),(4,5,2),(4,6,8),(4,7,4),(5,7,6),(7,6,1)])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
