#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from linklist import *

def reverse_k(L, k):
    if k <= 1:
        return L

    head = L
    tail = None
    i = j = L
    while i:
        c = 0
        while j and c < k:
            j = j.next
            c += 1
        if c < k:
            break
        h = j
        p = i
        while p != j:
            t = p
            p = p.next
            t.next = h
            h = t
        if tail:
            tail.next = h
        else:
            head = h
        tail = i
        i = j

    return head

def test(s, k):
    print('k:', k)
    L = parse_list(s)
    show_list(L, 'original list:')
    L = reverse_k(L, k)
    show_list(L, 'reversed list:')
    print('----')

def main():
    '''将单链表的每K个节点之间逆序'''
    test('1 2 3 4 5 6 7 8', 3)
    test('1 2 3 4 5 6 7 8', 2)
    test('1 2 3 4 5 6 7', 2)
    test('1 2 3 4 5 6 7', 5)
    test('1 2 3 4 5 6 7', 7)
    test('1 2 3 4 5 6 7', 8)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
