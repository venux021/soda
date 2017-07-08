#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bitree import BNode, parse_bitree
from q01 import pre_order_seq, in_order_seq

def test(s):
    tree = parse_bitree(s)
    print('pre:', ' '.join(pre_order_seq(tree)))
    print('in: ', ' '.join(in_order_seq(tree)))
    print('anti clock 1:', anti_clockwise_1(tree))
    print('anti clock 1 zcy:', anti_clockwise_1_zcy(tree))
    print('anti clock 2:', anti_clockwise_2(tree))

def anti_clockwise_2(tree):
    r = []
    anti_ck_2(tree, r)
    return r

def anti_ck_2(tree, r):
    if not tree:
        return
    r.append(str(tree.value))
    if tree.left and tree.right:
        anti_ck_left(tree.left, True, r)
        anti_ck_right(tree.right, True, r)
    elif tree.left:
        anti_ck_2(tree.left, r)
    else:
        anti_ck_2(tree.right, r)

def anti_ck_left(tree, pnt, r):
    if not tree:
        return
    if pnt or (not tree.left and not tree.right):
        r.append(str(tree.value))

    anti_ck_left(tree.left, pnt, r)
    anti_ck_left(tree.right, pnt and not tree.left, r)

def anti_ck_right(tree, pnt, r):
    if not tree:
        return
    anti_ck_left(tree.left, pnt and not tree.right, r)
    anti_ck_right(tree.right, pnt, r)
    if pnt or (not tree.left and not tree.right):
        r.append(str(tree.value))

def anti_clockwise_1(tree):
    height = get_height(tree)
    edges = [[None, None] for i in range(height)]
    get_edges(tree, edges, 0)
    r = []
    collect_edge(tree, 0, edges, r)
    return r

def anti_clockwise_1_zcy(tree):
    height = get_height(tree)
    edges = [[None, None] for i in range(height)]
    get_edges(tree, edges, 0)
    r = []
    for e in edges:
        r.append(str(e[0].value))
    collect_leaf(tree, 0, edges, r)
    for e in edges[::-1]:
        if e[0] != e[1]:
            r.append(str(e[1].value))
    return r

def collect_leaf(tree, level, edges, r):
    if not tree:
        return
    if tree.is_leaf() and tree not in edges[level]:
        r.append(tree.str_val())
    collect_leaf(tree.left, level+1, edges, r)
    collect_leaf(tree.right, level+1, edges, r)

def get_height(tree):
    if not tree:
        return 0
    return 1 + max(get_height(tree.left), get_height(tree.right))

def get_edges(tree, edges, level):
    if not tree:
        return
    if not edges[level][0]:
        edges[level][0] = tree
    edges[level][1] = tree
    get_edges(tree.left, edges, level+1)
    get_edges(tree.right, edges, level+1)

def collect_edge(tree, level, edges, r):
    if not tree:
        return
    r.append(str(tree.value))
    if tree.left and tree.right:
        collect_real(tree.left, level + 1, edges, r)
        collect_real(tree.right, level + 1, edges, r)
    elif tree.left:
        collect_edge(tree.left, level+1, edges, r)
    else:
        collect_edge(tree.right, level+1, edges, r)

def collect_real(tree, level, edges, r):
    if not tree:
        return
    if tree == edges[level][0]:
        r.append(str(tree.value))
    elif tree != edges[level][1] and tree.is_leaf():
        r.append(str(tree.value))

    collect_real(tree.left, level+1, edges, r)
    collect_real(tree.right, level+1, edges, r)

    if tree == edges[level][1] and tree != edges[level][0]:
        r.append(tree.str_val())

#def collect_right(tree, level, edges, r):
#    if not tree:
#        return
#    collect_right(tree.left, level+1, edges, r)
#    collect_right(tree.right, level+1, edges, r)
#    if tree == edges[level][1]:
#        r.append(str(tree.value))
#    elif not tree.left and not tree.right:
#        r.append(str(tree.value))

def main():
    '''打印二叉树的边界节点'''
    test('1 2 3 ## 4 5 6 7 8 9 10 ## ## ## ## ## 11 12 ## ## ## 13 14 15 16')
    test('1 2 3 4 5 ## ## 6 7 ## 12 8 9 10 11 ## 13 ## ## ## ## ## ## ## ## 14 ## 15 16 17 18 19 20')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
