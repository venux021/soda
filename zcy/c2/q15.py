#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')

from zcy.c3 import bitree

def to_dlist(tree):
    if not tree:
        return (None, None)

    left_head, left_tail = to_dlist(tree.left)
    if left_tail:
        left_tail.right = tree
        tree.left = left_tail

    right_head, right_tail = to_dlist(tree.right)
    if right_head:
        right_head.left = tree
        tree.right = right_head

    return (left_head if left_head else tree,
            right_tail if right_tail else tree)

def show_bi_list(L):
    p = L
    while p:
        print(p.value, '', end='')
        p = p.right
    print()

def test(s):
    tree = bitree.parse_bitree(s, value_conv = lambda x: int(x))
    L, T = to_dlist(tree)
    show_bi_list(L)

def main():
    '''将搜索二叉树转换成双向链表'''
    test('6 4 7 2 5 ## 9 1 3 ## ## 8')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
