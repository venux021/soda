#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bitree import *

def ca(tree, i, j):
    if not tree or tree.value == i or tree.value == j:
        return tree
    left = ca(tree.left, i, j)
    right = ca(tree.right, i, j)

    if left and right:
        return tree
    elif left:
        return left
    else:
        return right

def common_ancestor(tree, i, j):
    return ca(tree, i, j).value

def test(s, i, j):
    tree = parse_bitree(s, value_conv = lambda x: int(x))
    print('i: {}, j: {}, ancestor: {}'.format(i, j, common_ancestor(tree,i,j)))

def main():
    '''在二叉树中找到两个节点的最近公共祖先'''
    test('1 2 3 4 5 6 7 ## ## ## ## ## ## 8', 6, 8)
    test('1 2 3 4 5 6 7 ## ## ## ## ## ## 8', 5, 8)
    test('1 2 3 4 5 6 7 ## ## ## ## ## ## 8', 5, 2)
    test('1 2 3 4 5 6 7 ## ## ## ## ## ## 8', 1, 7)
    test('1 2 3 4 5 6 7 ## ## ## ## ## ## 8', 8, 3)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
