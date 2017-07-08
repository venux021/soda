#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bitree import *

def mst(tree):
    if not tree:
        return (None, 0)

    left = mst(tree.left)
    right = mst(tree.right)

    if left[0] == tree.left and right[0] == tree.right:
        if ((not tree.left or tree.value > tree.left.value)
                and (not tree.right or tree.value < tree.right.value)):
            return (tree, left[1] + right[1] + 1)
               
    if left[1] > right[1]:
        return left
    else:
        return right

def max_searching_tree(tree):
    node, count = mst(tree)
    if node:
        return (node.value, count)
    else:
        return None

def test(s):
    tree = parse_bitree(s, value_conv = lambda x: int(x))
    print('head of max searching tree:', max_searching_tree(tree))

def main():
    '''找到二叉树中的最大搜索二叉子树'''
    test('6 1 12 0 3 10 13 ## ## ## ## 4 14 20 16 2 5 11 15')
    test('6 10 12')
    test('6')
    test('6 3')
    test('6 ## 7')


if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
