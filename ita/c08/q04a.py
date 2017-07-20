#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def bucket_sort(arr):
    n = len(arr)
    k = n // 6
    if n % 6 > 0:
        k += 1
    bks = [[None,None] for i in range(k)]

    for v in arr:
        i = int(v * k)
        insert_sort(bks, i, v)

    head = tail = None
    for i in range(k):
        if bks[i][0]:
            if head is None:
                head = bks[i][0]
            else:
                tail.next = bks[i][0]
            tail = bks[i][1]

    p = head
    i = 0
    while p:
        arr[i] = p.value
        i += 1
        p = p.next

def insert_sort(bks, i, v):
    prev = None
    cur = bks[i][0]
    node = Node(v)
    while cur and cur.value < v:
        prev = cur
        cur = cur.next

    if prev:
        prev.next = node
    else:
        bks[i][0] = node

    if cur:
        node.next = cur
    else:
        bks[i][1] = node

def test(n):
    arr = [random.random() for i in range(n)]
    print('origin:', arr)
    bucket_sort(arr)
    print('sorted:', arr)

def main():
    '''实现桶排序'''
    test(10)
    test(20)
    test(30)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
