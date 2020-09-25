#!/usr/bin/env python3
import sys

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def nearest_common_ancestor(t, n1, n2):
    if not t:
        return
    elif t in (n1, n2):
        return t

    kL = nearest_common_ancestor(t.lc, n1, n2)
    kR = nearest_common_ancestor(t.rc, n1, n2)

    if not kL and not kR:
        return
    elif kL and kR:
        return t
    else:
        return kL or kR

@testwrapper
def test(seq, v1, v2):
    tree = new_bitree_level(seq)
    print_tree(tree)
    print(v1, v2)
    n1 = find_node_by_value(tree, v1)
    n2 = find_node_by_value(tree, v2)
    anc = nearest_common_ancestor(tree, n1, n2)
    print(f'Nearest common ancestor: {anc.value}')

def main():
    test([1,2,3,4,5,6,7,None,None,None,None,None,None,8], 4, 5)
    test([1,2,3,4,5,6,7,None,None,None,None,None,None,8], 4, 6)
    test([1,2,3,4,5,6,7,None,None,None,None,None,None,8], 8, 6)
    test([1,2,3,4,5,6,7,None,None,None,None,None,None,8], 8, 5)
    test([1,2,3,4,5,6,7,None,None,None,None,None,None,8], 1, 2)
    test([1,2,3,4,5,6,7,None,None,None,None,None,None,8], 3, 8)

if __name__ == '__main__':
    main()
