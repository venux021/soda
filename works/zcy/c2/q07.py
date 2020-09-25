#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from linklist import *

def is_parlindrome(L):
    if not L:
        return True
    elif not L.next:
        return True
    elif not L.next.next:
        return L.value == L.next.value

    a = b = L
    while a.next and a.next.next:
        a = a.next.next
        b = b.next

    mid = b
    right_list = reverse(mid.next)
    i = L
    j = right_list
    while j and j.value == i.value:
        j = j.next
        i = i.next

    result = not j

    reverse(right_list)

    return result

def reverse(L):
    if not L:
        return L
    h = None
    p = L
    while p:
        t = p
        p = p.next
        t.next = h
        h = t
    return h

def test(s):
    L = parse_list(s)
    print(s, is_parlindrome(L))
    print('origin list: ', end='')
    show_list(L)
    print('----')

def main():
    '''判断一个链表是否为回文结构'''
    test('1 2 3 4 5 4 3 2 1')
    test('1')
    test('2 2')
    test('1 2')
    test('1 2 1')
    test('1 2 3')
    test('1 2 3 3 2 1')
    test('1 2 2 1')
    test('1 2 3 4 3 2 2')
    test('1 2 3 4 2 1')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
