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
LEAF.lc = LEAF.rc = LEAF

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
    if p.rc != LEAF:
        p.rc.parent = p
    q.lc = p
    p.parent = q
    if parent:
        if k == 0:
            parent.lc = q
        else:
            parent.rc = q
    if q != LEAF:
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
    if p.lc != LEAF:
        p.lc.parent = p
    q.rc = p
    p.parent = q
    if parent:
        if k == 0:
            parent.lc = q
        else:
            parent.rc = q
    if q != LEAF:
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
    if root == LEAF or root is None:
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

def rb_remove(rbt, v):
    node = find_node(rbt, v)
    if node:
        rb_delete_node(rbt, node)

def find_node(tree, v):
    p = tree.root
    while p and p != LEAF and p.key != v:
        if p.key > v:
            p = p.lc
        else:
            p = p.rc
    if not p or p == LEAF:
        return None
    else:
        return p

def rb_delete_node(tree, node):
    if node == tree.root:
        if node.lc == LEAF and node.rc == LEAF:
            tree.root = None
            return
        elif node.lc == LEAF:
            tree.root = node.rc
            tree.root.parent = None
            tree.root.color = COLOR_BLACK
        elif node.rc == LEAF:
            tree.root = node.lc
            tree.root.parent = None
            tree.root.color = COLOR_BLACK
        else:
            x = node.rc
            while x.lc != LEAF:
                x = x.lc
            node.key = x.key
            if x != node.rc:
                x.parent.lc = x.rc
            else:
                node.rc = x.rc
            x.rc.parent = x.parent
            if x.color == COLOR_BLACK:
                rb_delete_fixup(tree, x.rc)
        return

    p = node.parent
    if node == p.lc:
        if node.lc == LEAF and node.rc == LEAF:
            p.lc = LEAF
            p.lc.parent = p
            if node.color == COLOR_BLACK:
                rb_delete_fixup(tree, p.lc)
        elif node.lc == LEAF:
            node.rc.parent = p
            p.lc = node.rc
            if node.color == COLOR_BLACK:
                rb_delete_fixup(tree, p.lc)
        elif node.rc == LEAF:
            node.lc.parent = p
            p.lc = node.lc
            if node.color == COLOR_BLACK:
                rb_delete_fixup(tree, p.lc)
        else:
            x = node.rc
            while x.lc != LEAF:
                x = x.lc
            node.key = x.key
            if x != node.rc:
                x.parent.lc = x.rc
            else:
                node.rc = x.rc
            x.rc.parent = x.parent
            if x.color == COLOR_BLACK:
                rb_delete_fixup(tree, x.rc)
    else:
        if node.lc == LEAF and node.rc == LEAF:
            p.rc = LEAF
            p.rc.parent = p
            if node.color == COLOR_BLACK:
                rb_delete_fixup(tree, p.rc)
        elif node.lc == LEAF:
            node.rc.parent = p
            p.rc = node.rc
            if node.color == COLOR_BLACK:
                rb_delete_fixup(tree, p.rc)
        elif node.rc == LEAF:
            node.lc.parent = p
            p.rc = node.lc
            if node.color == COLOR_BLACK:
                rb_delete_fixup(tree, p.rc)
        else:
            x = node.rc
            while x.lc != LEAF:
                x = x.lc
            node.key = x.key
            if x != node.rc:
                x.parent.lc = x.rc
            else:
                node.rc = x.rc
            x.rc.parent = x.parent
            if x.color == COLOR_BLACK:
                rb_delete_fixup(tree, x.rc)

def rb_delete_fixup(tree, node):
    while node != tree.root and node.color == COLOR_BLACK:
        if node == node.parent.lc:  # left child
            w = node.parent.rc
            if w.color == COLOR_RED:
                w.color = COLOR_BLACK
                node.parent.color = COLOR_RED
                if node.parent != tree.root:
                    left_rotate(node.parent)
                else:
                    tree.root = left_rotate(tree.root)
            elif w.lc.color == COLOR_BLACK and w.rc.color == COLOR_BLACK:
                w.color = COLOR_RED
                node = node.parent
            elif w.rc.color == COLOR_BLACK:
                if w.lc.color == COLOR_RED:
                    w.lc.color = COLOR_BLACK
                    w.color = COLOR_RED
                right_rotate(w)
            else:
                w.rc.color = COLOR_BLACK
                if node.parent.color == COLOR_RED:
                    w.color = COLOR_RED
                    node.parent.color = COLOR_BLACK
                if node.parent != tree.root:
                    left_rotate(node.parent)
                else:
                    tree.root = left_rotate(tree.root)
                node = tree.root
        else:  # right child
            w = node.parent.lc
            if w.color == COLOR_RED:
                w.color = COLOR_BLACK
                node.parent.color = COLOR_RED
                if node.parent != tree.root:
                    right_rotate(node.parent)
                else:
                    tree.root = right_rotate(tree.root)
            elif w.lc.color == COLOR_BLACK and w.rc.color == COLOR_BLACK:
                w.color = COLOR_RED
                node = node.parent
            elif w.lc.color == COLOR_BLACK:
                if w.rc.color == COLOR_RED:
                    w.rc.color = COLOR_BLACK
                    w.color = COLOR_RED
                left_rotate(w)
            else:
                w.lc.color = COLOR_BLACK
                if node.parent.color == COLOR_RED:
                    w.color = COLOR_RED
                    node.parent.color = COLOR_BLACK
                if node.parent != tree.root:
                    right_rotate(node.parent)
                else:
                    tree.root = right_rotate(tree.root)
                node = tree.root

    node.color = COLOR_BLACK

def test(n, rm_list = None):
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

#    rbt.dump()

    if not rm_list:
        rm_list = arr[:]
        random.shuffle(rm_list)
    print('rm: ', rm_list)
    rm_stat = []
    for v in rm_list:
#        rbt.dump()
#        print('remove:', v)
        rb_remove(rbt, v)
        rm_stat.append((v, validate_rbtree(rbt)))
    print('rm:', list(filter(lambda x: not x[1], rm_stat)))
    print('----')

def main():
    '''实现红黑树'''
    test(10)
    test(20)
    test(40)
    test(100)
#    test([18, 19, 20, 16, 14, 17, 15, 23, 22, 21])
#    test([21,26,27,20,28,23,25,24,22,19], [23,24,21,26,28,22,25,20,27,19])
#    test([7,2,4,9,5,8,11,10,6,3], [11,10,5,9,3,8,2,4,7,6])
#    test([13,17,9,15,11,22,24,23,18,6,8,14,21,19,25,12,10,16,7,20],
#            [24,12,18,25,19,15,6,14,11,10,8,17,16,22,7,20,13,23,9,21])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
