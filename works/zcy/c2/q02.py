#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from linklist import *

def drop_last_kth(L, k):
    if k <= 0:
        return L

    i = 0
    p = L
    while p and i < k-1:
        p = p.next
        i += 1
    if not p:
        return L

    d = L
    prev = None
    while p.next:
        p = p.next
        prev = d
        d = d.next

    if prev:
        prev.next = d.next
        return L
    else:
        return L.next

def drop_last_kth_d(L, k):
    if k <= 0:
        return L

    i = 0
    p = L
    while p and i < k - 1:
        p = p.next
        i += 1

    if not p:
        return L

    d = L
    while p.next:
        p = p.next
        d = d.next

    prev = d.prev
    if prev:
        prev.next = d.next
        if d.next:
            d.next.prev = prev
        return L
    else:
        if d.next:
            d.next.prev = None
        return L.next
        

def test(s, k):
    L = parse_list(s)
    print('k:', k)
    show_list(L)
    L = drop_last_kth(L, k)
    show_list(L)
    L = parse_list(s)
    L = drop_last_kth_d(L, k)
    show_list(L)
    print('------')

def main():
    '''在单链表和双链表中删除倒数第K个节点'''
    test('a b c d e', 3)
    test('a b c d e', 1)
    test('a b c d e', 0)
    test('a b c d e', 5)
    test('a b c d e', 6)
    test('a', 1)
    test('a', 2)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
