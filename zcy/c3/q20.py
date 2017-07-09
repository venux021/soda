#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bitree import *

def max_dist(tree):
    if not tree:
        return (0, 0)

    L = max_dist(tree.left)
    R = max_dist(tree.right)

    depth = max(L[0], R[0]) + 1
    dist = max(L[1], R[1], L[0] + R[0] + 1)

    return (depth, dist)

def test(s):
    tree = parse_bitree(s)
    print('max dist:', max_dist(tree)[1])

def main():
    '''二叉树节点间的最大距离问题'''
    test('1 2 3 4 5 6 7')
    test('1 2 ## 3 ## 4')
    test('1 2 5 3 ## 4')
    test('1 2 5 3 6 4 ## ## 7 8 ## ## 9')
    test('1 2 5 3 6 4 ## ## 7 8 ## 10 9 ## ##11 ## ## 12')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
