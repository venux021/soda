#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def is_post_seq(seq):
    if not seq:
        return True
    root = seq[-1]
    L = 0
    while seq[L] < root:
        L += 1
    left_size = L
    left_seq = seq[0:L]
    right_seq = seq[L:-1]
    for v in right_seq:
        if v < root:
            return False

    return is_post_seq(left_seq) and is_post_seq(right_seq)

def build_tree_post(seq):
    if not seq:
        return
    root = seq[-1]
    node = Node(value = seq[-1])
    L = 0
    while seq[L] < root:
        L += 1
    left_size = L
    left_seq = seq[0:L]
    right_seq = seq[L:-1]
    node.lc = build_tree_post(left_seq)
    node.rc = build_tree_post(right_seq)
    return node

@testwrapper
def test(seq):
    if not is_post_seq(seq):
        print(f'{seq} is not post seq')
        return
    tree = build_tree_post(seq)
    print_tree(tree)

def main():
    test([1,3,2,5,7,6,4])
    test([1,3,6,5,7,2,4])
    test([1,2,7,6,4])

if __name__ == '__main__':
    main()
