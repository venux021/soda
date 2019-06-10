#!/usr/bin/env python3
import sys

from sodacomm.bitree import new_bitree_level, print_tree_level
from sodacomm.tools import testwrapper

def upsideDown(root):
    if not root:
        return

    new_root, _ = doUpsideDown(root)
    return new_root

def doUpsideDown(root):
    if not root.left:
        # right child must be empty.
        # So, root is leaf now
        return (root, root)

    new_root, right_most = doUpsideDown(root.left)
    right_most.left = root.right
    right_most.right = root
    root.left = root.right = None
    return (new_root, root)

@testwrapper
def test(nums):
    tree = new_bitree_level(nums)
    print_tree_level(tree)
    tree = upsideDown(tree)
    print_tree_level(tree)

def main():
#    test([1,2,3,4,5])
#    test([1,2,None,4,5])
    test([1,2,3,4,5,None,None,6,None,None,None,7,8])

if __name__ == '__main__':
    main()
