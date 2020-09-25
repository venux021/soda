#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bitree import parse_bitree

def longest_path(tree, k):
    pm = {0: 0}
    return pre_order_path(tree, 1, pm, 0, 0, k)

def pre_order_path(tree, level, pm, cur_sum, max_len, k):
    if not tree:
        return max_len

    cur_sum += tree.value

    if cur_sum not in pm:
        pm[cur_sum] = level
    if (cur_sum - k) in pm:
        max_len = max(max_len, level - pm[cur_sum-k])

    left_len = pre_order_path(tree.left, level+1, pm, cur_sum, max_len, k)
    right_len = pre_order_path(tree.right, level+1, pm, cur_sum, max_len, k)

    if cur_sum in pm:
        del pm[cur_sum]

    return max(max_len, left_len, right_len)

def test(s, k):
    tree = parse_bitree(s, value_conv = lambda x: int(x))
    print(k, longest_path(tree, k))

def main():
    '''在二叉树中找到累加和为指定值的最长路径长度'''
    test('-3 3 -9 1 0 2 1 ## ## 1 6', 6)
    test('-3 3 -9 1 0 2 1 ## ## 1 6', -9)
    test('-3 3 -9 1 0 2 1 ## ## 1 6', 100)
    test('-3 3 -9 1 0 2 1 ## ## 1 6', -200)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
