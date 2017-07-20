#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

class SkipNode:

    def __init__(self, max_rank, value = None):
        self.max_rank = max_rank
        self.links = [None] * max_rank
        self.value = value

def sk_insert(head, rank, value):
    node = SkipNode(rank, value)
    prevs = []
    q = head
    i = head.max_rank - 1
    while i >= 0:
        while q.links[i] and q.links[i].value < value:
            q = q.links[i]
        prevs.append((i, q))
        i -= 1

    for i, q in prevs:
        if i < rank:
            node.links[i] = q.links[i]
            q.links[i] = node

def sk_print(head):
    for i in range(0, head.max_rank):
        print('rank:{} -> '.format(i), end = '')
        p = head.links[i]
        while p:
            print('(r={},{})'.format(p.max_rank, p.value), ' ', end = '')
            p = p.links[i]
        print()

def sk_find(head, value):
    i = head.max_rank - 1
    p = head
    while i >= 0:
        while p.links[i] and p.links[i].value <= value:
            p = p.links[i]
        if p.value == value:
            return p
        i -= 1
    return None

def test():
    head = SkipNode(6)
    nodes = [(1,2),(3,8),(2,10),(1,11),(4,13),(1,19),
             (2,20),(3,22),(1,23),(2,29)]
    random.shuffle(nodes)
    for n in nodes:
        sk_insert(head, n[0], n[1])
    print()

    sk_print(head)

    for i in [8, 11, 29, 2, 12, 15, 21, 24]:
        p = sk_find(head, i)
        if p:
            print('{} yes, rank = {}'.format(p.value, p.max_rank))
        else:
            print('{} no'.format(i))

def main():
    '''简单跳跃表'''
    test()

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
