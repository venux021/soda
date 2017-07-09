#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bitree import *

class TaskNode:
    def __init__(self, tree_node, index):
        self.tree = tree_node
        self.index = index

class DisjointSet:

    def __init__(self):
        self.father_map = {}
        self.rank_map = {}
        self.ancestor_map = {}

    def init_set(self, tree_node):
        self.father_map[tree_node] = tree_node
        self.rank_map[tree_node] = 0

    def set_ancestor(self, tree_node, ancestor):
        f = self.find_father(tree_node)
        self.ancestor_map[f] = ancestor

    def get_ancestor(self, tree_node):
        if tree_node not in self.father_map:
            return None
        f = self.find_father(tree_node)
        if f in self.ancestor_map:
            return self.ancestor_map[f]
        else:
            return None

    def find_father(self, tree_node):
        f = self.father_map[tree_node]
        while self.father_map[f] != f:
            f = self.father_map[f]
        father = f
        f = tree_node
        while f != father:
            t = f
            self.father_map[t] = father
            f = self.father_map[f]
        return father

    def merge(self, t1, t2):
        f1 = self.find_father(t1)
        f2 = self.find_father(t2)
        r1 = self.rank_map[f1]
        r2 = self.rank_map[f2]
        if r1 > r2:
            self.father_map[f2] = f1
        elif r1 < r2:
            self.father_map[f1] = f2
        else:
            self.father_map[f2] = f1
            self.rank_map[f1] += 1

def tarjan(tree, taskmap, diset, result):
    if not tree:
        return

    tarjan(tree.left, taskmap, diset, result)

    diset.init_set(tree)
    diset.set_ancestor(tree, tree)

    if tree.left:
        diset.merge(tree.left, tree)
        diset.set_ancestor(tree, tree)

    if tree in taskmap:
        for tsk in taskmap[tree]:
            peer = tsk.tree
            ancestor = diset.get_ancestor(peer)
            if ancestor:
                result[tsk.index] = ancestor
        del taskmap[tree]

    tarjan(tree.right, taskmap, diset, result)

    if tree.right:
        diset.merge(tree.right, tree)
        diset.set_ancestor(tree, tree)

def tarjan_query(tree, query):
    taskmap = {}
    result = [None] * len(query)
    for i, q in enumerate(query):
        if q[0] is None and q[1] is None:
            result[i] = None
        elif q[0] is None:
            result[i] = q[1]
        elif q[1] is None:
            result[i] = q[0]
        elif q[0] == q[1]:
            result[i] = q[0]
        else:
            a, b = q
            if a not in taskmap:
                taskmap[a] = []
            taskmap[a].append(TaskNode(b, i))
            if b not in taskmap:
                taskmap[b] = []
            taskmap[b].append(TaskNode(a, i))
            result[i] = None

    diset = DisjointSet()
    tarjan(tree, taskmap, diset, result)
    return result

def translate_query(tree, query):
    v2n = {}
    def _do(t):
        if t:
            v2n[t.value] = t
            _do(t.left)
            _do(t.right)
    _do(tree)
    q = []
    for qu in query:
        a = v2n[qu[0]] if qu[0] is not None else None
        b = v2n[qu[1]] if qu[1] is not None else None
        q.append((a,b))
    return q

def test(s, query):
    tree = parse_bitree(s, value_conv = lambda x: int(x))
    result = tarjan_query(tree, translate_query(tree, query))
    for i, t in enumerate(result):
        print('({},{})->{}'.format(query[i][0], query[i][1], t.value if t else None), end = ' ')
    print()

def main():
    '''Tarjan算法与并查集解决二叉树节点间最近公共祖先的批量查询问题'''
    test('1 2 3 4 5 ## 6 ## ## 7 8 9', [(4,7),(7,8),(8,9),(2,6),(5,7),(2,5),(3,6),(9,3),(8,3),(6,6),(None,5),(None,None)])
    test('1 2 ## 3 ## 4', [(3,2),(4,1)])
    test('1 ## 2 ## 3 ## 4', [(3,2),(4,1)])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
