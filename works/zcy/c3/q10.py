#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bitree import *

def test(s):
    tree = parse_bitree(s, value_conv = lambda x: int(x))
    r = [None, None]
    find_swap(tree, r)
    if r[0] and r[1]:
        print(r[0].value, r[1].value)
    else:
        print('not found')

def find_swap(tree, r):
    if not tree:
        return
    if tree.left and tree.left.value > tree.value:
        if not r[0]:
            r[0] = tree.left
        r[1] = tree
    if tree.right and tree.right.value < tree.value:
        if not r[0]:
            r[0] = tree
        r[1] = tree.right
    if not r[0]:
        find_swap(tree.left, r)
    if not r[0]:
        find_swap(tree.right, r)

def main():
    '''调整搜索二叉树中两个错误的节点'''
    test('8 15 5 3 6 10 20')
    test('8 6 15 3 5 10 20')
    test('8 5 15 6 3 10 20')
    test('15 5 8 3 6 10 20')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
