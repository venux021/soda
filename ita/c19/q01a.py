#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random
from collections import deque

class Node:

    def __init__(self, key):
        self.degree = 0
        self.key = key
        self.child = None
        self.sibling = None
        self.parent = None

    def prepend_child(self, c):
        if c.degree != self.degree:
            print('error child prepending')
            return
        c.sibling = self.child
        self.child = c
        c.parent = self
        self.degree += 1

class BinomialHeap:

    def __init__(self):
        self.head = None

    def push(self, key):
        if not self.head:
            self.head = Node(key)
        else:
            self.head = self.merge_heap(self.head, Node(key))

    def merge(self, h):
        self.head = self.merge_heap(self.head, h.head)

    def merge_heap(self, h1, h2):
        if h1 is None:
            return h2
        elif h2 is None:
            return h1

        hd = Node(0)
        tail = hd
        while h1 and h2:
            a, b = h1.degree, h2.degree
            if a <= b:
                t = h1
                h1 = h1.sibling
                tail.sibling = t
                tail = t
            if a >= b:
                t = h2
                h2 = h2.sibling
                tail.sibling = t
                tail = t
        if h1:
            tail.sibling = h1
        if h2:
            tail.sibling = h2

        prev = hd
        cur = hd.sibling
        nxt = cur.sibling
        while nxt:
            if cur.degree != nxt.degree:
                prev = cur
                cur = nxt
                nxt = nxt.sibling
            elif nxt.sibling and nxt.sibling.degree == nxt.degree:
                prev = cur
                cur = nxt
                nxt = nxt.sibling
            elif nxt.key <= cur.key:
                prev.sibling = nxt
                nxt.prepend_child(cur)
                cur = nxt
                nxt = nxt.sibling
            else:
                cur.sibling = nxt.sibling
                cur.prepend_child(nxt)
                nxt = cur.sibling

        return hd.sibling

    def dump(self):
        p = self.head
        while p:
            self._dump(p)
            p = p.sibling
        print('------')

    def _dump(self, root):
        q = deque()
        root.level = 1
        q.append(root)
        cur_level = 1
        while q:
            n = q.popleft()
            if n.level > cur_level:
                print()
                cur_level = n.level
            if n.degree > 1:
                print(' ' * (int(pow(2,n.degree-1))-1) * 5, end = '')
            print('{:5d}'.format(n.key), end = '')
            i = n.child
            while i:
                i.level = n.level + 1
                q.append(i)
                i = i.sibling
        print()
        print('*')

    def empty(self):
        return self.head is None

    def pop(self):
        pv = None
        s = p = self.head
        spv = None
        while p:
            if p.key < s.key:
                s = p
                spv = pv
            pv = p
            p = p.sibling
        
        if spv:
            spv.sibling = s.sibling
        else:
            self.head = s.sibling

        key = s.key
        hd = Node(0)
        tail = hd
        p = s.child
        while p:
            t = p
            p = p.sibling
            t.parent = None
            tail.sibling = t
            tail = t

        self.head = self.merge_heap(self.head, hd.sibling)
        return key

def make_heap(arr):
    hp = BinomialHeap()
    for a in arr:
        hp.push(a)
    return hp

def test(n):
    n1 = n
    n2 = random.randint(n//2, n*3//2)
    a1 = [random.randint(0,999) for i in range(n1)]
    a2 = [random.randint(0,999) for i in range(n2)]
    bh1 = make_heap(a1)
    bh1.dump()
    bh2 = make_heap(a2)
    bh2.dump()
    bh1.merge(bh2)
    bh1.dump()

    r = []
    while not bh1.empty():
        r.append(bh1.pop())
    print(a1)
    print(a2)
    print(r)

    for i in range(len(r)-1):
        if r[i] > r[i+1]:
            print('failed')
            break
    else:
        print('yes')

def main():
    '''二项堆'''
    test(250)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
