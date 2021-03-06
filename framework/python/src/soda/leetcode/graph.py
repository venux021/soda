# -*- coding: utf-8 -*-
import sys

MAX = sys.maxsize

class AdjNode:

    def __init__(self, adj, weight = None):
        self.adj = adj
        self.weight = weight
        self.next = None
        self.prev = None

Directed = 0
Undirected = 1

class AdjList:

    def __init__(self, vexes, edges, gtype = Directed):
        self.vexes = vexes[:]
        d2v = {}
        for i, v in enumerate(vexes):
            d2v[v] = i

        self.list = [AdjNode(-1) for i in range(len(vexes))]
        for e in edges:
            i = d2v[e[0]]
            j = d2v[e[1]]
            w = e[2] if len(e) == 3 else None
            self.add_edge(i, j, w)
            if gtype == Undirected:
                self.add_edge(j, i, w)
        self.d2v = d2v

    def add_vex(self, v):
        self.d2v[v] = self.size()
        self.vexes.append(v)
        self.list.append(AdjNode(-1))
        return self.d2v[v]

    def add_edge(self, i, j, w = None):
        anode = AdjNode(j, w)
        anode.next = self.list[i].next
        anode.prev = self.list[i]
        if self.list[i].next:
            self.list[i].next.prev = anode
        self.list[i].next = anode

    def vex_id(self, vex):
        return self.d2v[vex]

    def vex_name(self, vid):
        return self.vexes[vid]

    def size(self):
        return len(self.list)

    def first_adj(self, vid):
        return self.list[vid].next

    def adj_of(self, vid):
        p = self.first_adj(vid)
        while p:
            yield p
            p = p.next

    def iter_edges(self):
        for i in range(self.size()):
            for p in self.adj_of(i):
                yield (i, p.adj, p.weight)

    def dump(self):
        print('graph:')
        for i in range(self.size()):
            print('[{}] ->'.format(self.vex_name(i)), end=' ')
            p = self.first_adj(i)
            while p:
                if p.weight is None:
                    print(self.vex_name(p.adj), end=' ')
                else:
                    print('{}:{}'.format(self.vex_name(p.adj), p.weight), end=' ')
                p = p.next
            print()

    def clone(self):
        vexes = self.vexes[:]
        edges = []
        for i in range(self.size()):
            p = self.first_adj(i)
            while p:
                e = (self.vex_name(i), self.vex_name(p.adj), p.weight)
                edges.append(e)
                p = p.next
        return AdjList(vexes, edges)

    def clone_without_edges(self):
        vexes = self.vexes[:]
        edges = []
        return AdjList(vexes, edges)

    def adj_matrix(self):
        n = self.size()
        es = list(self.iter_edges())
        if len(es) == 0:
            return [[None] * n for i in range(n)]
        elif es[0][2] is None: # no weight
            mx = [[False] * n for i in range(n)]
            for e in es:
                mx[e[0]][e[1]] = True
            return mx
        else:
            mx = [[MAX] * n for i in range(n)]
            for e in es:
                mx[e[0]][e[1]] = e[2]
            return mx

    @staticmethod
    def parse(vexes, edges):
        return AdjList.parse_graph(vexes, edges, Directed)

    @staticmethod
    def parse_undirect(vexes, edges):
        return AdjList.parse_graph(vexes, edges, Undirected)

    @staticmethod
    def parse_graph(vexes, edges, gtype):
        vexes = AdjList.parse_vexes(vexes)
        edges = AdjList.parse_edges(edges)
        return AdjList(vexes, edges, gtype)

    @staticmethod
    def parse_vexes(vexes):
        if isinstance(vexes, str):
            vexes = vexes.split(' ')
        return vexes

    @staticmethod
    def parse_edges(edges):
        if isinstance(edges, str):
            e = []
            for f in edges.split(' '):
                f = f.strip()
                f = f.split(',')
                if len(f) == 2:
                    e.append((f[0], f[1]))
                elif len(f) == 3:
                    if f[2].find('.') >= 0:
                        w = float(f[2])
                    else:
                        w = int(f[2])
                    e.append((f[0], f[1], w))
            edges = e
        return edges


