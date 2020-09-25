#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from linklist import *

def list_add(L1, L2):
    L1 = reverse_list(L1)
    L2 = reverse_list(L2)
    i = L1
    j = L2
    h = ListNode()
    tail = h
    carry = 0
    while i and j:
        c = i.value + j.value + carry
        if c >= 10:
            carry = 1
            c -= 10
        else:
            carry = 0
        node = ListNode(c)
        tail.next = node
        tail = node
        i = i.next
        j = j.next

    if j:
        i = j

    while i:
        c = i.value + carry
        if c >= 10:
            carry = 1
            c -= 10
        else:
            carry = 0
        node = ListNode(c)
        tail.next = node
        tail = node
        i = i.next

    if carry == 1:
        tail.next = ListNode(1)

    reverse_list(L1)
    reverse_list(L2)

    return reverse_list(h.next)

def test(a, b):
    vc = lambda x: int(x)
    L1 = parse_list(a, vc)
    L2 = parse_list(b, vc)
    L3 = list_add(L1, L2)
    show_list(L1)
    show_list(L2)
    show_list(L3)
    print('----')

def main():
    '''两个单链表生成相加链表'''
    test('9 3 7', '6 3')
    test('9 9 7', '3')
    test('9 9 9 9', '1')
    test('1 2', '3 4')
    test('1 9', '3 4')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
