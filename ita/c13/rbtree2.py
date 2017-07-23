#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

COLOR_BLACK = 0
COLOR_RED = 1

class rbNode:
    def __init__(self, key, color, parent = None):
        self.key = key
        self.color = color
        self.lc = self.rc = None
        self.parent = parent

LEAF = rbNode(-1, COLOR_BLACK)
LEAF.lc = LEAF.rc = LEAF

class rbTree:

    def __init__(self):
        self.head = rbNode(0, COLOR_BLACK)
        self.head.lc = self.head.rc = LEAF

    def root(self):
        return self.head.lc
    def set_root(self, root):
        self.head.lc = root
        root.parent = self.head

    def new_node(self, key, color, parent = None):
        node = rbNode(key, color, parent)
        node.lc = node.rc = LEAF
        return node

    def dump(self):
        self._dump(self.root(), 1)
        print()
    def _dump(self, node, level):
        if node == LEAF:
            return
        print('{}|{}|{}'.format(node.key, 'R' if node.color == COLOR_RED else 'B', level), end = '')
        if node.lc != LEAF or node.rc != LEAF:
            print('(', end = '')
            self._dump(node.lc, level + 1)
            print(',', end = '')
            self._dump(node.rc, level + 1)
            print(')', end = '')

    def insert(self, key):
        if self.root() == LEAF:
            root = self.new_node(key, COLOR_BLACK)
            self.set_root(root)
            return

        p = self.root()
        x = None
        while True:
            if p.key == key:
                return
            elif p.key > key:
                if p.lc != LEAF:
                    p = p.lc
                else:
                    x = p.lc = self.new_node(key, COLOR_RED, p)
                    break
            else:
                if p.rc != LEAF:
                    p = p.rc
                else:
                    x = p.rc = self.new_node(key, COLOR_RED, p)
                    break
        self.insert_fixup(x)

    def insert_fixup(self, x):
        while x.parent.color == COLOR_RED:
            p = x.parent
            grand = p.parent
            if p == grand.lc:
                uncle = grand.rc
            else:
                uncle = grand.lc

            if uncle.color == COLOR_RED:
                p.color = uncle.color = COLOR_BLACK
                grand.color = COLOR_RED
                x = grand
            elif p == grand.lc:
                if x == p.rc:
                    p = left_rotate(p)
                    x = p.lc
                grand.color = COLOR_RED
                p.color = COLOR_BLACK
                right_rotate(grand)
            else:
                if x == p.lc:
                    p = right_rotate(p)
                    x = p.rc
                grand.color = COLOR_RED
                p.color = COLOR_BLACK
                left_rotate(grand)
        self.root().color = COLOR_BLACK

    def remove(self, key):
        n = self.find_key(key)
        if n == LEAF:
            return

        d = n
        if n.lc != LEAF and n.rc != LEAF:
            d = self.successor(n)
            n.key = d.key

        if d.lc != LEAF:
            x = d.lc
        else:
            x = d.rc

        p = d.parent
        if d == p.lc:
            p.lc = x
        else:
            p.rc = x
        x.parent = p

        if x == LEAF and p == self.head:
            # the last node has been removed, now it's a empty tree
            return

        if d.color == COLOR_BLACK:
            self.remove_fixup(x)

    def remove_fixup(self, x):
        while x != self.root() and x.color == COLOR_BLACK:
            p = x.parent
            if x == p.lc: # x is left child
                w = p.rc
                if w.color == COLOR_RED:
                    p.color = COLOR_RED
                    w.color = COLOR_BLACK
                    left_rotate(p)
                    p = x.parent
                    w = p.rc

                if w.lc.color == COLOR_BLACK and w.rc.color == COLOR_BLACK:
                    w.color = COLOR_RED
                    x = p
                    continue

                if w.rc.color == COLOR_BLACK:
                    w.color = COLOR_RED
                    w.lc.color = COLOR_BLACK
                    right_rotate(w)
                    w = p.rc

                w.rc.color = COLOR_BLACK
                if p.color == COLOR_RED:
                    w.color = COLOR_RED
                    p.color = COLOR_BLACK
                left_rotate(p)
                x = self.root()
            else: # x is right child
                w = p.lc
                if w.color == COLOR_RED:
                    p.color = COLOR_RED
                    w.color = COLOR_BLACK
                    right_rotate(p)
                    p = x.parent
                    w = p.lc

                if w.lc.color == COLOR_BLACK and w.rc.color == COLOR_BLACK:
                    w.color = COLOR_RED
                    x = p
                    continue

                if w.lc.color == COLOR_BLACK:
                    w.color = COLOR_RED
                    w.rc.color = COLOR_BLACK
                    left_rotate(w)
                    w = p.lc

                w.lc.color = COLOR_BLACK
                if p.color == COLOR_RED:
                    w.color = COLOR_RED
                    p.color = COLOR_BLACK
                right_rotate(p)
                x = self.root()

        x.color = COLOR_BLACK

    def successor(self, n):
        n = n.rc
        while n.lc != LEAF:
            n = n.lc
        return n

    def find_key(self, key):
        p = self.root()
        while p != LEAF:
            if p.key == key:
                break
            elif p.key < key:
                p = p.rc
            else:
                p = p.lc
        return p

def right_rotate(p):
    if p == LEAF or p.lc == LEAF:
        return

    s = p.parent
    L = p.lc
    Lrc = L.rc

    if p == s.lc:
        s.lc = L
    else:
        s.rc = L
    L.parent = s

    L.rc = p
    p.parent = L

    p.lc = Lrc
    if Lrc != LEAF:
        Lrc.parent = p

    return L

def left_rotate(p):
    if p == LEAF or p.rc == LEAF:
        return

    s = p.parent
    r = p.rc
    rlc = r.lc

    if p == s.lc:
        s.lc = r
    else:
        s.rc = r
    r.parent = s

    r.lc = p
    p.parent = r

    p.rc = rlc
    if rlc != LEAF:
        rlc.parent = p

    return r

def test(n, rm_list = None):
    if isinstance(n, int):
        a = random.randint(0,20)
        arr = [a + i for i in range(n)]
        random.shuffle(arr)
    else:
        arr = n
    print('arr:', arr)

    tree = rbTree()
    for v in arr:
        tree.insert(v)
#        print('validate after insert {}:'.format(v), validate_rbtree(tree))
#        tree.dump()
    print('validate:', validate_rbtree(tree))

    inorder_print(tree)

#    tree.dump()

    if not rm_list:
        rm_list = arr[:]
        random.shuffle(rm_list)
    print('rm: ', rm_list)
    rm_stat = []
    for v in rm_list:
#        tree.dump()
#        print('remove:', v)
        tree.remove(v)
        rm_stat.append((v, validate_rbtree(tree)))
    print('rm:', list(filter(lambda x: not x[1], rm_stat)))
    print('----')

def main():
    '''实现红黑树'''
    test(10)
    test(20)
    test(40)
    test(100)
#    test([21, 17, 20, 15, 22, 18, 14, 19, 23, 16])
#    test([18, 19, 20, 16, 14, 17, 15, 23, 22, 21])
#    test([21,26,27,20,28,23,25,24,22,19], [23,24,21,26,28,22,25,20,27,19])
#    test([7,2,4,9,5,8,11,10,6,3], [11,10,5,9,3,8,2,4,7,6])
#    test([13,17,9,15,11,22,24,23,18,6,8,14,21,19,25,12,10,16,7,20],
#            [24,12,18,25,19,15,6,14,11,10,8,17,16,22,7,20,13,23,9,21])
#    test([23, 18, 20, 15, 28, 26, 27, 16, 17, 14, 24, 30, 25, 13, 22, 31, 19, 21, 29, 32], [18, 17, 32, 25, 19, 14, 27, 15, 24, 13, 22, 16, 23, 21, 26, 20, 30, 28, 31, 29])

def inorder_print(rbt):
    inorder(rbt.root())
    print()

def inorder(root):
    if root != LEAF:
        inorder(root.lc)
        print(root.key, ' ', end = '')
        inorder(root.rc)

def validate_rbtree(tree):
    return valid(tree.root()) > 0

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


if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()

