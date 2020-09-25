#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

class ListNode:

    def __init__(self, value, link = None):
        self.value = value
        self.link = link

def tarjan_query(t, queries, answers):
    query_map = {}
    index_map = {}
    for index, q in enumerate(queries):
        n1, n2 = q
        query_map[n1.value] = ListNode(n2.value, link = query_map.get(n1.value))
        query_map[n2.value] = ListNode(n1.value, link = query_map.get(n2.value))
        index_map[n1.value] = ListNode(index, link = index_map.get(n1.value))
        index_map[n2.value] = ListNode(index, link = index_map.get(n2.value))

    ancestor_map = {} # collection leader -> ancestor

    dst = DisjointSet([n.value for n in get_all_nodes(t)])

    def _do_process(node):
        if node.lc:
            _do_process(node.lc)
            dst.merge(node.lc.value, node.value)
        
        leader = dst.find_leader(node.value)
        ancestor_map[leader] = node.value

        p = query_map.get(node.value)
        q = index_map.get(node.value)
        while p:
            L = dst.find_leader(p.value)
            if L in ancestor_map:
                answers[q.value] = ancestor_map[L]
            p = p.link
            q = q.link
        query_map.pop(node.value, None)

        if node.rc:
            _do_process(node.rc)
            dst.merge(node.rc.value, node.value)

        leader = dst.find_leader(node.value)
        ancestor_map[leader] = node.value

    _do_process(t)

class DSNode:

    def __init__(self, name, leader = None):
        self.name = name
        self.rank = 0
        self.leader = leader

class DisjointSet:

    def __init__(self, values):
        self.vm = {}
        for v in values:
            self.vm[v] = DSNode(v, leader = v)

    def merge(self, v1, v2):
        L1 = self.find_leader(v1)
        L2 = self.find_leader(v2)
        if self.vm[L1].rank > self.vm[L2].rank:
            self.vm[L2].leader = L1
        elif self.vm[L1].rank < self.vm[L2].rank:
            self.vm[L1].leader = L2
        else:
            self.vm[L1].leader = L2
            self.vm[L2].rank += 1

    def find_leader(self, v):
        p = p0 = self.vm[v]
        while self.vm[p.leader] != p:
            p = self.vm[p.leader]
        while p0 != p:
            k = self.vm[p0.leader]
            p0.leader = p.name
            p0 = k
        return p.name

@testwrapper
def test(seq, queries):
    tree = new_bitree_level(seq)
    print_tree(tree)
    nq = [(find_node_by_value(tree, n1), find_node_by_value(tree, n2)) for n1, n2 in queries]
    print([(n1.value, n2.value) for n1, n2 in nq])
    answers = [None] * len(queries)
    tarjan_query(tree, nq, answers)
    print(answers)

def main():
    test([1,2,3,4,5,None,6,None,None,7,8,9], [(4,7),(7,8),(8,9),(9,3),(2,8),(4,9)])

if __name__ == '__main__':
    main()
