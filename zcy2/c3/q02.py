#!/usr/bin/env python3
from collections import deque
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def print_edge_1(t):
    if not t:
        return
    height = get_height(t)
    left = [None] * (height + 1)
    right = [None] * (height + 1)
    qu = deque()
    qu.append((t, 1))
    max_level = 0
    last_node = None
    while qu:
        node, level = qu.popleft()
        if level > max_level:
            left[level] = node
            print(node.value, end = ' ')
            max_level = level
            if last_node:
                right[level-1] = last_node
        last_node = node
        if node.lc:
            qu.append((node.lc, level + 1))
        if node.rc:
            qu.append((node.rc, level + 1))
    right[max_level] = last_node

    print_inner_leaf(t, 1, left, right)

    for i in range(len(right)-1, 1, -1):
        print(right[i].value, end = ' ')

    print('')

def print_inner_leaf(t, level, left, right):
    if not t:
        return
    if not t.lc and not t.rc and left[level] != t and right[level] != t:
        print(t.value, end = ' ')
    print_inner_leaf(t.lc, level + 1, left, right)
    print_inner_leaf(t.rc, level + 1, left, right)

def print_edge_2(t):
    if not t:
        return
    print(t.value, end = ' ')
    if t.lc and t.rc:
        print_left_edge(t.lc, True)
        print_right_edge(t.rc, True)
    elif t.lc:
        print_edge_2(t.lc)
    else:
        print_edge_2(t.rc)

def print_left_edge(t, isprint):
    if not t:
        return
    if isprint or not t.lc and not t.rc:
        print(t.value, end = ' ')
    print_left_edge(t.lc, isprint)
    print_left_edge(t.rc, isprint and not t.lc)

def print_right_edge(t, isprint):
    if not t:
        return
    print_right_edge(t.lc, isprint and not t.rc)
    print_right_edge(t.rc, isprint)
    if isprint or t.isleaf:
        print(t.value, end = ' ')

@testwrapper
def test(seq):
    tree = new_bitree_level(seq)
    print_tree(tree)
    print_edge_1(tree)
    print_edge_2(tree)
    print('')

def main():
    test([1,2,3,None,4,5,6,7,8,9,10,None,None,None,None,None,11,12,None,None,None,13,14,15,16])

if __name__ == '__main__':
    main()
