#!/usr/bin/env python3
import sys

from sodacomm.graph import AdjList

MAX = sys.maxsize

class Edge:

    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.w = w

def show_2nd_mst(g):
    n = g.size()
    E = []
    V = set([0])
    min_e = []

    for p in g.adj_of(0):
        E.append(Edge(0, p.adj, p.weight))

    me = [[0] * n for i in range(n)]

    c = 1
    cost = 0
    while c < n:
        mi = select_min(E, V)
        min_e.append((mi.a, mi.b))
        cost += mi.w
        for i in V:
            me[i][mi.b] = max(mi.w, me[i][mi.a])
        mi.w = MAX
        V.add(mi.b)
        for p in g.adj_of(mi.b):
            if p.adj not in V:
                E.append(Edge(mi.b, p.adj, p.weight))
        c += 1

    print('min cost tree')
    for e in min_e:
        print(g.vex_name(e[0]), g.vex_name(e[1]))
    print('total cost:', cost)

    cn = MAX
    L = 0
    a = b = None
    for i, j, w in g.iter_edges():
        if me[i][j] == w:
            print('mst not unique')
        else:
            A = cost - me[i][j] + w
            if A < cn:
                cn = A
                L = me[i][j]
                a = i
                b = j
    print('2nd: replace edge[length={}] with ({},{}), cost: {}'.format(
                L, g.vex_name(a), g.vex_name(b), cn))

def select_min(E, V):
    i = 0
    for j in range(1, len(E)):
        if E[j].b not in V and E[j].w < E[i].w:
            i = j
    return E[i]

def test(vex, edge):
    g = AdjList.parse_undirect(vex, edge)
    show_2nd_mst(g)

def main():
    '''次优最小生成树'''
    test('a b c d e f g h i',
            'a,b,4 a,h,8 b,c,8 b,h,11 c,d,7 c,f,4 c,i,2 d,e,9 d,f,14 e,f,10 f,g,2 g,i,6 g,h,1 h,i,7')

if __name__ == '__main__':
    main()
