#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bitree import *

def _pre_in(pre, pb, pe, ins, ib, ie):
    n = pe - pb + 1
    if n == 0:
        return None

    root_value = pre[pb]
    split = ib
    while ins[split] != root_value:
        split += 1

    left_size = split - ib
    right_size = ie - split

    root_node = BNode(root_value)

    root_node.left = _pre_in(pre, pb+1, pb+left_size, ins, ib, split-1)
    root_node.right = _pre_in(pre, pb+left_size+1, pe, ins, split+1, ie)

    return root_node

def pre_in(pre, ins):
    return _pre_in(pre, 0, len(pre)-1, ins, 0, len(ins)-1)

def _in_post(ins, ib, ie, post, pb, pe):
    n = ie - ib + 1
    if n == 0:
        return None

    root_value = post[pe]
    split = ie
    while ins[split] != root_value:
        split -= 1

    right_size = ie - split
    left_size = n - 1 - right_size

    root_node = BNode(root_value)
    root_node.left = _in_post(ins, ib, split-1, post, pb, pb+left_size-1)
    root_node.right = _in_post(ins, split+1, ie, post, pe-right_size, pe-1)
    return root_node

def in_post(ins, post):
    return _in_post(ins, 0, len(ins)-1, post, 0, len(post)-1)

def _pre_post(pre, ai, aj, post, bi, bj):
    n = aj - ai + 1
    if n <= 0:
        return None

    root_value = pre[ai]
    root_node = BNode(root_value)
    if n == 1:
        return root_node

    k = bj - 1
    if post[k] == pre[ai+1]:
        root_node.left = _pre_post(pre, ai+1, aj, post, bi, bj-1)
    else:
        while post[k] != pre[ai+1]:
            k -= 1
        left_size = k - bi + 1
        right_size = n - left_size - 1

        root_node.left = _pre_post(pre, ai+1, ai+left_size, post, bi, k)
        root_node.right = _pre_post(pre, ai+left_size+1, aj, post, k+1, bj-1)

    return root_node

def pre_post(pre, post):
    return _pre_post(pre, 0, len(pre)-1, post, 0, len(post)-1)

def test(pre, in_, post):
    pre = pre.split(' ')
    in_ = in_.split(' ')
    post = post.split(' ')

    t1 = pre_in(pre, in_)
    t2 = in_post(in_, post)
    t3 = pre_post(pre, post)

    pre_order_print(t1)
    in_order_print(t1)
    print('%')
    pre_order_print(t2)
    in_order_print(t2)
    print('%')
    pre_order_print(t3)
    in_order_print(t3)
    print('-----')

def main():
    '''先序、中序和后序数组两两结合重构二叉树'''
    test('1 2 4 5 3 6 7', '4 2 5 1 6 3 7', '4 5 2 6 7 3 1')
    test('1 3 6 7', '1 6 3 7', '6 7 3 1')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
