#!/usr/bin/env python3
import sys

from sodacomm.graph import AdjList

class EdgeNode:

    def __init__(self, u, v, w):
        # selected
        self.u = u

        # unselected
        self.v = v

        self.w = w

class EdgeHeap:

    def __init__(self, num_vex):
        self.size = 0
        self.num_vex = num_vex
        self.nodes = [[None] * num_vex for i in range(num_vex)]
        self.h = [None] * (num_vex * (num_vex-1) + 1)
        self.selected = [False] * num_vex

    def push(self, u, v, w):
        if not self.nodes[u][v]:
            self.nodes[u][v] = self.nodes[v][u] = EdgeNode(u,v,w)
            node = self.nodes[u][v]
            self.size += 1
            self.h[self.size] = node
            self.adjust_up(self.size)

    def dump(self):
        for i in range(1, self.size+1):
            n = self.h[i]
            print('{},{},{}'.format(n.u,n.v,n.w), end = ' ')
        print()

    def adjust_up(self, pos):
        while pos > 1:
            p = pos // 2
            if self.h[p].w > self.h[pos].w:
                self.swap(p, pos)
                pos = p
            else:
                break

    def swap(self, a, b):
        t = self.h[a]
        self.h[a] = self.h[b]
        self.h[b] = t

    def adjust_down(self, pos):
        while True:
            L = pos * 2
            R = L + 1
            if L > self.size:
                break
            elif L == self.size or self.h[L].w < self.h[R].w:
                child = L
            else:
                child = R
            if self.h[pos].w > self.h[child].w:
                self.swap(pos, child)
                pos = child
            else:
                break

    def pop(self):
        while True:
            t = self.do_pop()
            if not t or not self.selected[t.u] or not self.selected[t.v]:
                if t:
                    self.selected[t.u] = self.selected[t.v] = True
                return t

    def do_pop(self):
        if self.size == 0:
            return
        t = self.h[1]
        self.h[1] = self.h[self.size]
        self.size -= 1
        self.adjust_down(1)
        return t

def show_mst(g):
    n = g.size()
    hp = EdgeHeap(n)
    max_edge = [[0] * n for i in range(n)]
    selected = set([0])

    mst_edge = []
    for p in g.adj_of(0):
        hp.push(0, p.adj, p.weight)

    for i in range(n-1):
        e = hp.pop()
        mst_edge.append(e)
        for j in selected:
            max_edge[j][e.v] = max_edge[e.v][j] = max(e.w, max_edge[j][e.u])
        selected.add(e.v)
        v = e.v
        for p in g.adj_of(v):
            hp.push(v, p.adj, p.weight)

    print('MST:', end = ' ')
    cost = 0
    for e in mst_edge:
        print('{},{}'.format(g.vex_name(e.u), g.vex_name(e.v)), end = ' ')
        cost += e.w
    print()
    print('cost:', cost)

    E = [[False] * n for i in range(n)]
    for e in mst_edge:
        E[e.u][e.v] = E[e.v][e.u] = True

    min_cost = sys.maxsize
    min_edge = None
    for i,j,w in g.iter_edges():
        if not E[i][j]:
            E[i][j] = E[j][i] = True
            if w == max_edge[i][j]:
                print('has more than one MST')
            else:
                C = cost - max_edge[i][j] + w
                if C < min_cost:
                    min_cost = C
                    min_edge = (i, j)

    print('second minimal tree: replace edge[{}] of {}'.format(
                max_edge[min_edge[0]][min_edge[1]], 
                (g.vex_name(min_edge[0]), g.vex_name(min_edge[1]))
        ))

def test(vex, edge):
    g = AdjList.parse_undirect(vex, edge)
    show_mst(g)

def main():
    '''最小生成树和次优最小生成树'''
    test('a b c d e f g h i',
            'a,b,4 a,h,8 b,c,8 b,h,11 c,d,7 c,f,4 c,i,2 d,e,9 d,f,14 e,f,10 f,g,2 g,i,6 g,h,1 h,i,7')

if __name__ == '__main__':
    main()
