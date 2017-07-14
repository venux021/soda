# -*- coding: utf-8 -*-

class AdjNode:

    def __init__(self, adj, weight = None):
        self.adj = adj
        self.weight = weight
        self.next = None

class VexNode:

    def __init__(self, value):
        self.value = value
        self.first_adj = None

class AdjList:

    def __init__(self, vexes, edges):
        self.list = [None] * len(vexes)
        d2v = {}
        for i, v in enumerate(vexes):
            self.list[i] = VexNode(v)
            d2v[v] = i
        for e in edges:
            i = d2v[e[0]]
            j = d2v[e[1]]
            w = e[2] if len(e) == 3 else None
            anode = AdjNode(j, w)
            anode.next = self.list[i].first_adj
            self.list[i].first_adj = anode
        self.d2v = d2v

    def vex_id(self, vex):
        return self.d2v[vex]

    def vex_name(self, vid):
        return self.list[vid].value

    def size(self):
        return len(self.list)

    def first_adj(self, vid):
        return self.list[vid].first_adj

    def dump(self):
        print('graph:')
        for i in range(self.size()):
            print('[{}] ->'.format(self.vex_name(i)), end=' ')
            p = self.first_adj(i)
            while p:
                print('{}:{}'.format(self.vex_name(p.adj), p.weight), end=' ')
                p = p.next
            print()

    @staticmethod
    def parse(vexes, edges):
        if isinstance(vexes, str):
            vexes = vexes.split(' ')
        return AdjList(vexes, edges)


