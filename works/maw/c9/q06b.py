#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from graph import *

class Node:
    def __init__(self, v):
        self.v = v
        self.next = None
        self.prev = None

def euler_circuit(g):
    n = g.size()
    visited = [[False] * n for i in range(n)]
    pts = [g.first_adj(i) for i in range(n)]
    head = Node(-1)
    p = Node(0)
    head.next = p
    p.prev = head

    while p:
        i = p.v
        tail = H = Node(i)
        while True:
            q = pts[i]
            if not q:
                break
            pts[i] = q.next
            if visited[i][q.adj]:
                continue
            visited[i][q.adj] = visited[q.adj][i] = True
            node = Node(q.adj)
            tail.next = node
            node.prev = tail
            tail = node
            i = q.adj

        if tail != H:
            H = H.next
            nxt = p.next
            p.next = H
            H.prev = p
            if nxt:
                tail.next = nxt
                nxt.prev = tail

        p = p.next

    r = []
    p = head.next
    while p:
        r.append(g.vex_name(p.v))
        p = p.next

    return r

def test(vex, edge):
    g = AdjList.parse_undirect(vex, edge)
    print(euler_circuit(g))

def main():
    '''欧拉回路'''
    test([1,2,3,4,5,6,7,8,9,10,11,12],
            [(1,3),(1,4),(2,3),(2,8),
             (3,4),(3,7),(3,6),(3,9),
             (4,5),(4,7),(4,10),(4,11),
             (5,10),(6,9),(7,9),(7,10),
             (8,9),(9,10),(9,12),(10,11),
             (10,12)])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
