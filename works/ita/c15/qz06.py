#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from collections import deque
sys.path.append('../..')

from zcy.c3.bitree import *

def get_list_recur(tree, sup):
    if not tree:
        return 0

    if sup:
        C1 = 0
        C1 += get_list_recur(tree.left, False)
        C1 += get_list_recur(tree.right, True)
        return C1
    else:
        # present
        C1 = tree.score
        C1 += get_list_recur(tree.left, True)
        C1 += get_list_recur(tree.right, False)

        # not present
        C2 = get_list_recur(tree.left, False) + get_list_recur(tree.right, False)
        return max(C1, C2)

def get_list(tree):
#    return max(get_list_recur(tree, False), get_list_recur(tree, True))
#    set_parent(tree)
    nodes = nodes_by_level(tree)
    mtrue = {} # supervisor present
    mfalse = {} # supervisor present

    ctrue = {}
    cfalse = {}

    for n in nodes[::-1]:
        c0 = 0
        c1 = n.score
        c2 = 0
        if n.left:
            c0 += mfalse[n.left]
            c1 += mtrue[n.left]
            c2 += mfalse[n.left]
        if n.right:
            c0 += mtrue[n.right]
            c1 += mfalse[n.right]
            c2 += mfalse[n.right]

        if c1 >= c2:
            mfalse[n] = c1
            cfalse[n] = 1
        else:
            mfalse[n] = c2
            cfalse[n] = 0
        mtrue[n] = c0

        ctrue[n] = 0

    name_list = []
    if mfalse[tree] >= mtrue[tree]:
        collect_employees(tree, False, name_list, cfalse)
    else:
        collect_employees(tree, True, name_list, cfalse)

    return name_list

def collect_employees(tree, sup, name_list, cfalse):
    if not tree:
        return
    if sup:
        collect_employees(tree.left, False, name_list, cfalse)
        collect_employees(tree.right, True, name_list, cfalse)
    elif cfalse[tree]:
        name_list.append(tree.value)
        collect_employees(tree.left, True, name_list, cfalse)
        collect_employees(tree.right, False, name_list, cfalse)
    else:
        collect_employees(tree.left, False, name_list, cfalse)
        collect_employees(tree.right, False, name_list, cfalse)

def nodes_by_level(tree):
    q = deque()
    q.append(tree)
    nodes = []
    while q:
        n = q.popleft()
        nodes.append(n)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    return nodes

def set_parent(tree):
    if tree.left:
        tree.left.parent = tree
        set_parent(tree.left)
    if tree.right:
        tree.right.parent = tree
        set_parent(tree.right)

def test(s, values):
    tree = parse_bitree(s)
    set_values(tree, values)
    print(get_list(tree))

def set_values(tree, values):
    q = deque()
    q.append(tree)
    i = 0
    while q:
        n = q[0]
        n.score = values[i]
        i += 1
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
        q.popleft()

def main():
    '''公司聚会计划'''
    test('A B C D E F G H I J K',
            [10, 7, 9, 8, 6, 17, 9, 10, 6, 8, 9])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
