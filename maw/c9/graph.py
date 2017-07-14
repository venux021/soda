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

    def __init__(self, size):
        self.size = size
        self.list = [None] * size
        self.d2v = {}

    def add_vex(self, i, data):
        self.list[i] = VexNode(data)
        self.d2v[data] = self.list[i]

    def vex_id(self, data):
        return self.d2v[data]

    def add_edge(self, di, dj):
        i = self.vex_id(di)
        j = self.vex_id(dj)
        anode = AdjNode(j)
        anode.next = self.list[i].first_arc
        self.list[i].first_arc = anode

    @staticmethod
    def parse(vexes, edges):
        if isinstance(vexes, str):
            vexes = vexes.split(' ')
        n = len(vexes)
        graph = AdjList(n)
        for i in range(n):
            graph.add_vex(i, vexes[i])

        for e in edges:
            graph.add_edge(e[0], e[1])

        return graph


