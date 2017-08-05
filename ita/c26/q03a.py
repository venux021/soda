#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('../..')

from maw.c9 import graph

from q02a import max_flow

def max_bin_match(edges):
    left = set([e[0] for e in edges])
    right = set([e[1] for e in edges])

    vex = list(left | right) + ['s', 't']
    es = []
    for e in edges:
        es.append((e[0], e[1], 1))
    for i in left:
        es.append(('s', i, 1))
    for i in right:
        es.append((i, 't', 1))

    g = graph.AdjList.parse(vex, es)
    max_flow(g, g.vex_id('s'), g.vex_id('t'))

def test(edges):
    max_bin_match(edges)

def main():
    '''最大二分匹配'''
    test([(1,2),(3,2),(3,6),(5,4),(5,6),(5,8),(7,6),(9,6)])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
