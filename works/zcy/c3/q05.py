#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from bitree import *

def morris_in(tree):
    p = tree

    while p:
        k = p.left
        if k:
            while k.right and k.right != p:
                k = k.right
            if k.right == p:
                k.right = None
            else:
                k.right = p
                p = p.left
                continue
        print(p.str_val(), '', end = '')
        p = p.right

    print()

def morris_pre(tree):
    p = tree
    while p:
        k = p.left
        if k:
            while k.right and k.right != p:
                k = k.right
            if k.right == p:
                k.right = None
            else:
                print(p.str_val(), '', end = '')
                k.right = p
                p = p.left
                continue
        else:
            print(p.str_val(), '', end = '')
        p = p.right
    print()

def morris_post(tree):
    p = tree
    while p:
        k = p.left
        if k:
            while k.right and k.right != p:
                k = k.right
            if k.right == p:
                k.right = None
                reverse_print_right_path(p.left)
            else:
                k.right = p
                p = p.left
                continue
        else:
            pass
        p = p.right

    reverse_print_right_path(tree)
    print ()

def reverse_print_right_path(tree):
    h = None
    p = tree
    while p:
        k = p.right
        p.right = h
        h = p
        p = k

    p = h
    h = None
    while p:
        print(p.str_val(), '', end = '')
        k = p.right
        p.right = h
        h = p
        p = k

def test(s):
    tree = parse_bitree(s)

    print('morris pre: ', end = '')
    morris_pre(tree)

    print('morris in:  ', end = '')
    morris_in(tree)

    print('morris post:', end = '')
    morris_post(tree)

def main():
    '''遍历二叉树的神级方法'''
    test('4 2 6 1 3 5 7')
    test('1 2 ## 3')
    test('1 ## 2 ## 3')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
