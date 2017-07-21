#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

COLOR_RED = 0
COLOR_BLACK = 1

class rbNode:
    def __init__(self, key, color):
        self.key = key
        self.lc = self.rc = None
        self.parent = None
        self.color = color
    @staticmethod
    def new(key, color):
        node = rbNode(key, color)
        node.lc = node.rc = LEAF
        return node

LEAF = rbNode(-1, COLOR_BLACK)

class rbTree:
    def __init__(self):
        self.root = None

    def dump(self):
        self._dump(self.root, 1)
        print()

    def _dump(self, node, level):
        if not node or node == LEAF:
            return
        print('{}|{}|{}'.format(node.key, 'R' if node.color == COLOR_RED else 'B', level), end = '')
        if node.lc != LEAF or node.rc != LEAF:
            print('(', end = '')
            self._dump(node.lc, level + 1)
            print(',', end = '')
            self._dump(node.rc, level + 1)
            print(')', end = '')

def make_rbtree(arr):
    tree = rbTree()
    for v in arr:
        rb_insert(tree, v)
#        tree.dump()
    return tree

def rb_insert(tree, key):
    node = binary_insert(tree, key)
    if node:
        fixup(tree, node)

def binary_insert(tree, key):
    if not tree.root:
        tree.root = rbNode.new(key, COLOR_RED)
        return tree.root

    p = tree.root
    while True:
        if p.key == key:
            return None
        elif p.key > key:
            if p.lc == LEAF:
                p.lc = rbNode.new(key, COLOR_RED)
                p.lc.parent = p
                return p.lc
            else:
                p = p.lc
        else:
            if p.rc == LEAF:
                p.rc = rbNode.new(key, COLOR_RED)
                p.rc.parent = p
                return p.rc
            else:
                p = p.rc

def fixup(tree, node):
    p = node
    while p.color == COLOR_RED:
        if not p.parent:
            p.color = COLOR_BLACK
            break
        elif p.parent.color == COLOR_BLACK:
            break
        
        # p.parent.color is COLOR_RED
        grand = p.parent.parent
        if p.parent == grand.lc:
            if grand.rc.color == COLOR_RED:
                grand.lc.color = grand.rc.color = COLOR_BLACK
                grand.color = COLOR_RED
                p = grand
            else:
                if p == p.parent.rc:
                    left_rotate(p.parent)
                p = grand
                t = right_rotate(p)
                p.color = COLOR_RED
                t.color = COLOR_BLACK
                if p == tree.root:
                    tree.root = t
                p = t
        else:
            if grand.lc.color == COLOR_RED:
                grand.lc.color = grand.rc.color = COLOR_BLACK
                grand.color = COLOR_RED
                p = grand
            else:
                if p == p.parent.lc:
                    right_rotate(p.parent)
                p = grand
                t = left_rotate(p)
                p.color = COLOR_RED
                t.color = COLOR_BLACK
                if p == tree.root:
                    tree.root = t
                p = t

def left_rotate(node):
    if node.parent:
        if node.parent.lc == node:
            k = 0  # left
        else:
            k = 1  # right 

    parent = node.parent
    p = node
    q = node.rc
    p.rc = q.lc
    p.rc.parent = p
    q.lc = p
    p.parent = q
    if parent:
        if k == 0:
            parent.lc = q
        else:
            parent.rc = q
    q.parent = parent
    return q

def right_rotate(node):
    if node.parent:
        if node.parent.lc == node:
            k = 0
        else:
            k = 1
    parent = node.parent
    p = node
    q = node.lc
    p.lc = q.rc
    p.lc.parent = p
    q.rc = p
    p.parent = q
    if parent:
        if k == 0:
            parent.lc = q
        else:
            parent.rc = q
    q.parent = parent
    return q

def inorder_print(rbt):
    inorder(rbt.root)
    print()

def inorder(root):
    if root and root != LEAF:
        inorder(root.lc)
        print(root.key, ' ', end = '')
        inorder(root.rc)

def validate_rbtree(tree):
    return valid(tree.root) > 0

def valid(root):
    if root == LEAF:
        return 1

    if root.color == COLOR_RED:
        if root.lc.color == COLOR_RED or root.rc.color == COLOR_RED:
            return -1

    left_h = valid(root.lc)
    if left_h < 0:
        return -1
    right_h = valid(root.rc)
    if right_h < 0:
        return -1
    if left_h != right_h:
        return -1
    elif root.color == COLOR_BLACK:
        return left_h + 1
    else:
        return left_h

def test(n):
    if isinstance(n, int):
        a = random.randint(0,20)
        arr = [a + i for i in range(n)]
        random.shuffle(arr)
    else:
        arr = n
    print('arr:', arr)
    rbt = make_rbtree(arr)
    print('validate:', validate_rbtree(rbt))
    inorder_print(rbt)
    print('----')

def main():
    '''实现红黑树'''
    test(10)
    test(20)
    test(40)
#    test([18, 19, 20, 16, 14, 17, 15, 23, 22, 21])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
