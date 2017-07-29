#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random
from collections import deque

class Node:

    def __init__(self, t):
        self.t = t
        self.parent = None
        self.keys = [0] * (2*t-1)
        self.child = [None] * 2*t
        self.num_keys = 0
        self.leaf = True

    def is_full(self):
        return self.num_keys == 2*self.t-1

    def insert_key(self, key):
        i = self.num_keys
        while i > 0 and key < self.keys[i-1]:
            self.keys[i] = self.keys[i-1]
            i -= 1
        self.keys[i] = key
        self.num_keys += 1

    def update(self, pos, left, new_key, right):
        for i in range(self.num_keys, pos, -1):
            self.keys[i] = self.keys[i-1]
            self.child[i+1] = self.child[i]
        self.keys[pos] = new_key
        self.child[pos] = left
        self.child[pos+1] = right
        self.num_keys += 1

    def text(self):
        return '  ' + ','.join(map(str, self.keys[:self.num_keys])) + '  '

    def text_width(self):
        return len(self.text())

    def list_children(self):
        if self.num_keys:
            return self.child[:self.num_keys+1]
        else:
            return []

class BTree:

    def __init__(self, degree):
        self.dg = degree
        self.root = None

    def new_node(self):
        return Node(self.dg)

    def insert(self, key):
        if not self.root:
            self.root = self.new_node()
            self.root.insert_key(key)
            return

        if self.root.is_full():
            n1, k, n2 = self.split(self.root)
            self.root = self.new_node()
            self.root.leaf = False
            self.root.insert_key(k)
            self.root.child[0] = n1
            self.root.child[1] = n2
            n1.parent = n2.parent = self.root

        p = self.root
        while True:
            if p.leaf:
                p.insert_key(key)
                break

            i = 0
            while i < p.num_keys and key > p.keys[i]:
                i += 1

            if i < p.num_keys and key == p.keys[i]:
                break

            if p.child[i].is_full():
                n1, k, n2 = self.split(p.child[i])
#                print(i, p.text(), n1.text(), k, n2.text())
                p.update(i, n1, k, n2)
                if key > p.keys[i]:
                    i += 1
            p = p.child[i]

    def split(self, node):
        left = node
        right = self.new_node()
        right.parent = left.parent
        right.leaf = left.leaf

        new_key = left.keys[node.t-1]

        right.keys[0:node.t-1] = left.keys[node.t:node.t*2-1]
        right.child[0:node.t] = left.child[node.t:node.t*2]
        right.num_keys = node.t - 1

        left.num_keys = node.t - 1

        return (left, new_key, right)

    def dump(self):
        self.collect_width(self.root)
        self.root.level = 1
        q = deque([self.root])
        cur_level = 1
        while q:
            n = q[0]
            if n.level != cur_level:
                print()
                cur_level = n.level
            q.popleft()

            num_blanks = (n.width - n.text_width()) // 2
            blank_str = ' ' * num_blanks
            print(blank_str + n.text() + blank_str, end = '')

            if not n.leaf:
                for c in n.list_children():
                    c.level = n.level + 1
                    q.append(c)
        print()
            

    def collect_width(self, node):
        if not node.leaf:
            w = 0
            for c in node.list_children():
                w += self.collect_width(c)
            node.width = max(w, node.text_width())
        else:
            node.width = node.text_width()
        return node.width


def test(t):
    keys = [i for i in range(1, 60)]
    random.shuffle(keys)

    tree = BTree(t)
    for k in keys:
        tree.insert(k)
#        tree.dump()

    tree.dump()

def main():
    '''B树操作'''
    test(4)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
