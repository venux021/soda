#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def make_parent(t):
    if t.lc:
        t.lc.parent = t
        make_parent(t.lc)
    if t.rc:
        t.rc.parent = t
        make_parent(t.rc)

def find_next_in_order(n):
    if n.rc:
        p = n.rc
        while p.lc:
            p = p.lc
        return p
    p = n
    while p.parent:
        if p == p.parent.lc:
            return p.parent
        p = p.parent

@testwrapper
def test(seq, v):
    tree = new_bitree_level(seq)
    make_parent(tree)
    tree.parent = None
    print_tree(tree)
    node = find_node_by_value(tree, v)
    if not node:
        print(f'node {v} not found')
        return
    print(f'node: {v}')
    next_node = find_next_in_order(node)
    if next_node:
        print(f'next node is {next_node.value}')
    else:
        print('next node not found')

def main():
    test([4,2,6,1,3,5,7], 4)
    test([4,2,6,1,3,5,7], 2)
    test([4,2,6,1,3,5,7], 3)
    test([4,2,6,1,3,5,7], 1)
    test([4,2,6,1,3,5,7], 7)

if __name__ == '__main__':
    main()
