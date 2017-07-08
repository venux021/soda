#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bitree import *

class TPnode:
    def __init__(self, binode, L = 0, R = 0):
        self.node = binode
        self.left_count = L
        self.right_count = R
        self.left = self.right = None
    def value(self):
        return self.node.value
    def topo_contrib(self):
        return self.left_count + self.right_count + 1

def _max_topo(tree):
    if not tree:
        return None
    left = _max_topo(tree.left)
    right = _max_topo(tree.right)

    if left:
        p = left
        left_count = left.left_count + left.right_count + 1
        while p and p.value() < tree.value:
            p = p.right
        if p:
            left_count -= (p.left_count + p.right_count + 1)
    else:
        left_count = 0

    if right:
        p = right
        right_count = right.topo_contrib()
        while p and p.value() > tree.value:
            p = p.left
        if p:
            right_count -= p.topo_contrib()
    else:
        right_count = 0

    thisnode = TPnode(tree, left_count, right_count)
    thisnode.left = left
    thisnode.right = right
    return thisnode

def max_topo_size(tree):
    tpnode = _max_topo(tree)
    return tpnode.left_count + tpnode.right_count + 1

def test(s):
    tree = parse_bitree(s, value_conv = lambda x: int(x))
    print(s)
    print('max topo size:', max_topo_size(tree))
    print('------')

def main():
    '''找到二丈树中符合搜索二叉树条件的最大拓扑结构'''
    test('6 1 12 0 3 10 13 ## ## ## ## 4 14 20 16 2 5 11 15')
    test('6 10 12')
    test('6')
    test('6 3')
    test('6 ## 7')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
