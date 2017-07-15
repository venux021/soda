# -*- coding: utf-8 -*-

class AdjNode:

    def __init__(self, adj, weight = None):
        self.adj = adj
        self.weight = weight
        self.next = None
        self.prev = None

class AdjList:

    def __init__(self, vexes, edges):
        self.vexes = vexes[:]
        d2v = {}
        for i, v in enumerate(vexes):
            d2v[v] = i

        self.list = [AdjNode(-1) for i in range(len(vexes))]
        for e in edges:
            i = d2v[e[0]]
            j = d2v[e[1]]
            w = e[2] if len(e) == 3 else None
            anode = AdjNode(j, w)
            anode.next = self.list[i].next
            anode.prev = self.list[i]
            if self.list[i].next:
                self.list[i].next.prev = anode
            self.list[i].next = anode
        self.d2v = d2v

    def vex_id(self, vex):
        return self.d2v[vex]

    def vex_name(self, vid):
        return self.vexes[vid]

    def size(self):
        return len(self.list)

    def first_adj(self, vid):
        return self.list[vid].next

    def dump(self):
        print('graph:')
        for i in range(self.size()):
            print('[{}] ->'.format(self.vex_name(i)), end=' ')
            p = self.first_adj(i)
            while p:
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

    @staticmethod
    def parse(vexes, edges):
        if isinstance(vexes, str):
            vexes = vexes.split(' ')
        return AdjList(vexes, edges)


