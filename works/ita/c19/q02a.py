#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random
import math

NODES = []

class Node:

    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.mark = False
        self.prev = self.next = None
        self.child = None
        self.parent = None
        NODES.append(self)

    def add_child(self, ch):
        self.degree += 1
        if self.child:
            nxt = self.child.next
            ch.next = nxt
            nxt.prev = ch
            self.child.next = ch
            ch.prev = self.child
        else:
            self.child = ch
            ch.prev = ch.next = ch
        ch.parent = self

    def take_child(self, c):
        if not self.child:
            return
        t = p = self.child
        while p != c:
            if p.next == t:
                break
            p = p.next
        if p == c:
            if c.next != c:
                prv = p.prev
                nxt = p.next
                prv.next = nxt
                nxt.prev = prv
                if self.child == c:
                    self.child = nxt
            else:
                self.child = None
            self.degree -= 1
            return c

class FibHeap:

    def __init__(self):
        self.size = 0
        self.min_node = None

    def empty(self):
        return self.size == 0

    def push(self, key):
        if self.size == 0:
            n = Node(key)
            n.prev = n.next = n
            self.min_node = n
            self.size = 1
            return

        n = Node(key)
        nxt = self.min_node.next
        n.next = nxt
        nxt.prev = n
        self.min_node.next = n
        n.prev = self.min_node
        if n.key < self.min_node.key:
            self.min_node = n
        self.size += 1

    def top(self):
        if self.size:
            return self.min_node.key

    def pop(self):
        if self.size == 0:
            return

        n = self.min_node
        if n.child:
            p = n.child
            t = p
            while True:
                p.parent = None
                if p.next == t:
                    break
                p = p.next
            self.merge_list(self.min_node, t)
        self.drop(n)
        self.size -= 1

        if self.size > 0:
            sz = int(math.log(self.size)/math.log(2)) + 1
            A = [None] * sz
            roots = set(self.all_roots())
            while roots:
                x = roots.pop()
                d = x.degree
                while A[d]:
                    y = A[x.degree]
                    if y in roots:
                        roots.remove(y)
                    if x.key > y.key:
                        tmp = x
                        x = y
                        y = tmp
                    self.drop(y)
                    x.add_child(y)
                    y.mark = False
                    A[d] = None
                    d += 1
                A[d] = x

            self.min_node = None
            H = Node(-1)
            H.prev = H.next = H
            for a in A:
                if a:
                    if self.min_node is None or self.min_node.key > a.key:
                        self.min_node = a
                    nxt = H.next
                    a.next = nxt
                    nxt.prev = a
                    H.next = a
                    a.prev = H
            head = H.next
            tail = H.prev
            tail.next = head
            head.prev = tail

        return n.key

    def all_roots(self):
        roots = []
        p = self.min_node
        t = p
        while self.min_node:
            roots.append(p)
            if p.next == t:
                break
            p = p.next
        return roots

    def drop(self, node):
        if node.next == node:
            self.min_node = None
            return
        elif node == self.min_node:
            self.min_node = node.next

        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv

    def merge_list(self, a, b):
        btail = b.prev
        nxt = a.next
        btail.next = nxt
        nxt.prev = btail
        a.next = b
        b.prev = a

    def dump(self):
        if self.size == 0:
            print('<empty fib heap>')
            return
        p = self.min_node
        while True:
            self._dump(p, 0)
            if p.next == self.min_node:
                break
            p = p.next
        print('----')

    def _dump(self, node, level):
        print(' ' * level * 4, end = '')
        print('{:4d}'.format(node.key))
        p = node.child
        if p:
            t = p
            while True:
                self._dump(p, level+1)
                if p.next == t:
                    break
                p = p.next

    def decrease_key(self, node, new_key):
        node.key = new_key
        # not violate heap rule
        if not node.parent or node.parent.key <= new_key:
            return

        # node is root
        p = node.parent
        if not p:
            if new_key < self.min_node.key:
                self.min_node = node
            return

        # cut node from parent
        p.take_child(node)
        self.add_to_roots(node)

        while p and p.parent:
            if not p.mark:
                p.mark = True
                break
            t = p.parent
            t.take_child(p)
            self.add_to_roots(p)
            p = t

    def add_to_roots(self, node):
        node.prev = node.next = node
        node.parent = None
        self.merge_list(self.min_node, node)
        if node.key < self.min_node.key:
            self.min_node = node

    def remove_node(self, node):
        self.decrease_key(node, -0x7fffffff)
        self.pop()

def test(n):
    arr = [random.randint(0,100) for i in range(n)]
    arr = [92, 29, 97, 93, 3, 4, 66, 55, 5, 32, 98, 94, 40, 21, 99, 69, 79, 4, 70, 9]

    fib_heap = FibHeap()
    print(arr)
    for v in arr:
        fib_heap.push(v)

    pop = fib_heap.pop()
    print('min:', pop)

    fib_heap.dump()
    node = random.choice(NODES)
    while node.key == pop:
        node = random.choice(NODES)
    print('random node:', node.key)
    choose_key = node.key

    try:
        fib_heap.decrease_key(node, -99)
        fib_heap.dump()
    except:
        print(arr, choose_key)
        raise

    fib_heap.pop()
    fib_heap.dump()

#    fib_heap.remove_node(node)
#    fib_heap.dump()

#    print('pop min:', fib_heap.pop())
#    print('min:', fib_heap.top())
#    fib_heap.dump()
#
#    r = []
#    while not fib_heap.empty():
#        r.append(fib_heap.pop())
#
#    print(r)


def main():
    '''斐波那契堆'''
    test(20)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
