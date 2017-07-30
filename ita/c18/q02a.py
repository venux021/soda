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

    def drop_key_at(self, pos):
        for i in range(pos+1, self.num_keys):
            self.keys[i-1] = self.keys[i]
            self.child[i] = self.child[i+1]
        self.num_keys -= 1

    def pop_right(self):
        if self.num_keys > 0:
            key = self.keys[self.num_keys-1]
            child = self.child[self.num_keys]
            self.num_keys -= 1
            return (key, child)

    def push_left(self, key, child):
        self.child[self.num_keys+1] = self.child[self.num_keys]
        for i in range(self.num_keys, 0, -1):
            self.keys[i] = self.keys[i-1]
            self.child[i] = self.child[i-1]
        self.keys[0] = key
        self.child[0] = child
        self.num_keys += 1

    def pop_left(self):
        if self.num_keys > 0:
            key = self.keys[0]
            child = self.child[0]
            for i in range(1, self.num_keys):
                self.keys[i-1] = self.keys[i]
                self.child[i-1] = self.child[i]
            self.child[self.num_keys-1] = self.child[self.num_keys]
            self.num_keys -= 1
            return (key, child)

    def push_right(self, key, child):
        self.keys[self.num_keys] = key
        self.child[self.num_keys+1] = child
        self.num_keys += 1

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
        if not self.root:
            print('<empty B-tree>')
            return
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

    def remove(self, key):
        return self.remove_key(self.root, key)

    def remove_key(self, node, key):
        if not node:
            return False

        i = 0
        while i < node.num_keys and node.keys[i] < key:
            i += 1

        if node.leaf:
            if i < node.num_keys and node.keys[i] == key:
                node.drop_key_at(i)
                if node == self.root and node.num_keys == 0:
                    self.root = None
                return True
            return False

        if i < node.num_keys and node.keys[i] == key:  # not leaf
            lc = node.child[i]
            rc = node.child[i+1]
            if lc.num_keys >= lc.t:
                p = lc
                while not p.leaf:
                    p = p.child[p.num_keys]
                dk = node.keys[i] = p.keys[p.num_keys-1]
                return self.remove_key(lc, dk)
            elif rc.num_keys >= rc.t:
                p = rc
                while not p.leaf:
                    p = p.child[0]
                dk = node.keys[i] = p.keys[0]
                return self.remove_key(rc, dk)
            else:
                self.merge(lc, node.keys[i], rc)
                node.drop_key_at(i)
                if node == self.root and node.num_keys == 0:
                    self.root = lc
                return self.remove_key(lc, key)

        T = self.dg
        if node.child[i].num_keys < T:
            if i > 0 and node.child[i-1].num_keys >= T:
                k, ch = node.child[i-1].pop_right()
                node.child[i].push_left(node.keys[i-1], ch)
                node.keys[i-1] = k
                return self.remove_key(node.child[i], key)
            elif i < node.num_keys and node.child[i+1].num_keys >= T:
                k, ch = node.child[i+1].pop_left()
                node.child[i].push_right(node.keys[i], ch)
                node.keys[i] = k
                return self.remove_key(node.child[i], key)
            elif i > 0:  # node.child[i] has left subling
                left_sib = node.child[i-1]
                self.merge(left_sib, node.keys[i-1], node.child[i])
                node.drop_key_at(i-1)
                if node == self.root and node.num_keys == 0:
                    self.root = left_sib
                return self.remove_key(left_sib, key)
            else: # i == 0, merge node.child[0] and node.child[1]
                child = node.child[0]
                self.merge(child, node.keys[0], node.child[1])
                node.drop_key_at(0)
                # node.child[0] not modified
                if node == self.root and node.num_keys == 0:
                    self.root = child
                return self.remove_key(child, key)

        return self.remove_key(node.child[i], key)

    def merge(self, n1, key, n2):
        x1 = n1.num_keys
        x2 = n2.num_keys
        n1.keys[x1] = key
        n1.keys[x1+1:x1+1+x2] = n2.keys[:x2]
        n1.child[x1+1:x1+x2+2] = n2.child[:x2+1]
        n1.num_keys += (x2 + 1)


def test(t):
    keys = [i for i in range(1, 50)]
    random.shuffle(keys)

    create_keys = keys[:]

    random.shuffle(keys)
    remove_keys = keys[:]

#    create_keys = [19, 6, 29, 3, 2, 27, 25, 16, 12, 4, 17, 14, 15, 8, 20, 22, 10, 9, 13, 21, 24, 11, 7, 1, 18, 26, 23, 28, 5]
#    remove_keys = [22, 1, 2, 3, 12, 20, 14, 7, 19, 13, 25, 23, 16, 18, 24, 29, 8, 28, 21, 5, 27, 6, 4, 10, 17, 11, 9, 15, 26]

    print('create_keys =', create_keys)
    print('remove_keys =', remove_keys)

    tree = BTree(t)
    for k in create_keys:
        tree.insert(k)

    tree.dump()

    remove_keys.extend([-1,0,-100,300])
    random.shuffle(remove_keys)
    for k in remove_keys:
        if not tree.remove(k):
            print('failed to remove', k)
#        print('\nremove {}'.format(k))
#        tree.dump()
#        print('--------')

def main():
    '''B树操作'''
    test(3)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
