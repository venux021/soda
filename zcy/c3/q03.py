#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bitree import * 

def print_tree(tree, level, ch = None):
    if not tree:
        return

    print_tree(tree.right, level+1, 0)

    for i in range(level):
        print('     ', end = '')

    if level == 0:
        print('H{}H'.format(tree.str_val()))
    elif ch == 0:
        print('R{}R'.format(tree.str_val()))
    else:
        print('L{}L'.format(tree.str_val()))

    print_tree(tree.left, level+1, 1)

def test(s):
    tree = parse_bitree(s)
    pre_order_print(tree)
    in_order_print(tree)
    print_tree(tree, 0)

def main():
    '''如何较为直观地打印二叉树'''
    test('1 2 3 4 ## 5 6 ## 7')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
