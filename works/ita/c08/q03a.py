#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

def test(n):
    arr = [random.randint(1000, 9999) for i in range(n)]
    print('1:', arr)
    radix_sort(arr, 4)
    print('2:', arr)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def radix_sort(arr, k):
    n = len(arr)
    head = Node(-1)
    tail = head
    for v in arr:
        node = Node(v)
        tail.next = node
        tail = node

    for r in range(1, k+1):
        process(head, r)

    p = head.next
    i = 0
    while p:
        arr[i] = p.value
        p = p.next
        i += 1

class RNode:
    def __init__(self):
        self.head = self.tail = None

def process(head, r):
    s = [RNode() for i in range(10)]
    while head.next:
        p = head.next
        head.next = p.next
        p.next = None

        i = bit_number_r10(p.value, r)
        if s[i].head:
            s[i].tail.next = p
        else:
            s[i].head = p
        s[i].tail = p

    tail = None
    for i in range(10):
        if not s[i].head:
            continue
        if not tail:
            head.next = s[i].head
        else:
            tail.next = s[i].head
        tail = s[i].tail

def bit_number_r10(n, r):
    for i in range(r-1):
        n = n // 10
    return n % 10

def main():
    '''实现基数排序'''
    test(10)
    test(30)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
