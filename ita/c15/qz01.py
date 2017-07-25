#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('../..')

from maw.c9.graph import *

MAX = 0x7fffffff

def show_longest_path(g, s, e):
    n = g.size()
    dp = [[MAX] * n for i in range(n)]
    path = [[-1] * n for i in range(n)]

    for i in range(n):
        dp[i][i] = 0
        p = g.first_adj(i)
        while p:
            dp[i][p.adj] = p.weight
            path[i][p.adj] = i
            p = p.next

    for k in range(n):
        for i in range(n):
            for j in range(n):
                a = dp[i][k]
                b = dp[k][j]
                if a < MAX and b < MAX and (dp[i][j] == MAX or dp[i][j] < a + b):
                    dp[i][j] = a + b
                    path[i][j] = path[k][j]

    print(dp[s][e])
    step = []
    p = e
    while p >= 0:
        step.append(g.vex_name(p))
        p = path[s][p]
    print(step[::-1])

def dump_mx(mx):
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            if mx[i][j] < MAX:
                print('{:4d}'.format(mx[i][j]), end = '')
            else:
                print('   *', end = '')
        print()

def test(vex, edge, start, end):
    g = AdjList.parse(vex, edge)
    show_longest_path(g, g.vex_id(start), g.vex_id(end))

def main():
    '''有向无环图最长简单路径'''
    test('A B C D E F G',
            [('A','B',1),('A','C',2),
             ('B','D',3),('C','D',1),
             ('D','E',4),('B','E',5),
             ('C','E',2),('C','F',2),
             ('F','E',3),
             ('F','G',1),('G','E',2),('G','B',1)],
         'A', 'E')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
