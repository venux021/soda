# -*- coding: utf-8 -*-

class AdjNode:

    def __init__(self, adj):
        self.adj = adj
        self.next = None

class VexNode:

    def __init__(self, value):
        self.value = value
        self.first_adj = None

class AdjList:

    def __init__(self, vexes, edges):
        self.list = [None] * size
        d2v = {}
        for i, v in enumerate(vexes):
            self.list[i] = VexNode(v)
            d2v[v] = i
        for e in edges:
            i = d2v[e[0]]
            j = d2v[e[1]]
            anode = AdjNode(j)
            anode.next = self.list[i].first_arc
            self.list[i].first_arc = anode

    @staticmethod
    def parse(vexes, edges):
        if isinstance(vexes, str):
            vexes = vexes.split(' ')
        return AdjList(vexes, edges)


