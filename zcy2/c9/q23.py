#!/usr/bin/env python3
from collections import deque
import random
import sys

from sodacomm.tools import testwrapper

class Node:

    def __init__(self, value = None):
        self.value = value
        self.lc = self.rc = self.parent = None

def dump(root):
    qu = deque([(root,1)])
    while qu:
        f,level = qu.popleft()
        if f:
            print(f'{f.value}:{level}', end = ' ')
            qu.append((f.lc,level+1))
            qu.append((f.rc,level+1))
        else:
            print(f'#:{level}', end = ' ')
    print('')

class BiHeap:

    def __init__(self):
        self.head = self.tail = None
        self.size = 0
        self.level = 1

    def insert(self, num):
        if self.size == 0:
            self.head = self.tail = Node(num)
            self.size = 1
            self.level = 1
            return
        if self.size == 2 ** self.level - 1:
            n = self.most_left(self.head)
            self.tail = n.lc = Node(num)
            self.tail.parent = n
            self.level += 1
        elif self.tail == self.tail.parent.lc:
            p = self.tail.parent
            self.tail = p.rc = Node(num)
            self.tail.parent = p
        else:
            p = self.tail.parent
            while p == p.parent.rc:
                p = p.parent
            n = self.most_left(p.parent.rc)
            self.tail = n.lc = Node(num)
            self.tail.parent = n
        self.size += 1
        p = self.tail
        while p.parent and p.parent.value > p.value:
            p.parent.value, p.value = p.value, p.parent.value
            p = p.parent

    def pop(self):
        if self.size == 0:
            return
        res = self.head.value
        if self.size == 1:
            self.head = self.tail = None
            self.size = 0
            self.level = 0
            return res

        self.head.value = self.tail.value
        if self.size == 2 ** (self.level-1):
            self.tail.parent.lc = None
            self.tail = self.most_right(self.head)
            self.level -= 1
        elif self.tail == self.tail.parent.rc:
            p = self.tail.parent
            p.rc = None
            self.tail = p.lc
        else:
            p = self.tail.parent
            p.lc = None
            while p == p.parent.lc:
                p = p.parent
            n = self.most_right(p.parent.lc)
            self.tail = n

        self.size -= 1
        p = self.head
        while p.lc or p.rc:
            if not p.rc or p.lc.value < p.rc.value:
                t = p.lc
            else:
                t = p.rc
            if p.value > t.value:
                p.value, t.value = t.value, p.value
                p = t
            else:
                break
        return res

    def most_left(self, n):
        while n.lc:
            n = n.lc
        return n

    def most_right(self, n):
        while n.rc:
            n = n.rc
        return n

@testwrapper
def test(arr):
    print(arr)
    bp = BiHeap()
    for i in range(len(arr)//2):
        bp.insert(arr[i])
    while bp.size > 0:
        print(bp.pop(), end = ' ')
    print('')
    for i in range(len(arr)//2, len(arr)):
        bp.insert(arr[i])
    while bp.size > 0:
        print(bp.pop(), end = ' ')
    print('')

def main():
    test([3,9,2,4,8,5,6,7,1])

if __name__ == '__main__':
    main()
