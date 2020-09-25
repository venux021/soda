#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bitree import *

def left_path_len(tree):
    p = tree
    n = 0
    while p:
        p = p.left
        n += 1
    return n

def right_path_len(tree):
    p = tree
    n = 0
    while p:
        p = p.right
        n += 1
    return n

def total_nodes(tree):
    p = tree
    total = 0
    while True:
        left_len = left_path_len(p)
        right_len = right_path_len(p)
        if left_len == right_len:
            total += ((1 << left_len) - 1)
            break
        else:
            lc_r_path = right_path_len(p.left)
            if lc_r_path == left_len - 1:
                total += (1 << (left_len-1))
                p = p.right
            else:
                total += (1 << (right_len-1))
                p = p.left
    return total

def test(s):
    tree = parse_bitree(s)
    print('total nodes:', total_nodes(tree))

def main():
    '''统计完全二叉树的节点数'''
    test('1')
    test('1 2 3 4 5 6 7 8')
    test('1 2 3 4 5 6 7 8 9 10')
    test('1 2 3 4 5 6 7 8 9 10 11')
    test('1 2 3 4 5 6 7 8 9 10 11 12')
    test('1 2 3 4 5 6 7 8 9 10 11 12 13')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
