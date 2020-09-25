#!/usr/bin/env python3
import random
import sys

from sodacomm.linklist import *
from sodacomm.tools import testwrapper

def complex_copy(slist):
    if not slist:
        return None
    p = slist
    while p:
        t = Node(p.value, next = p.next)
        t.rand = p.rand
        p.next = t
        p = t.next

    p = slist.next
    while True:
        if p.rand:
            p.rand = p.rand.next
        if p.next:
            p = p.next.next
        else:
            break

    head = tail = None
    p = slist
    while p:
        t = p.next
        p.next = t.next
        if not head:
            head = tail = t
        else:
            tail.next = t
            tail = t
            t.next = None
        p = p.next
    return head

def make_rand(slist):
    nodes = []
    p = slist
    while p:
        nodes.append(p)
        p = p.next
    for n in nodes:
        r = random.randint(0,100)
        if r > 50:
            i = random.choice(nodes)
            n.rand = i
        else:
            n.rand = None
    return slist

def print_rand(slist):
    print_list(slist)
    for n in iter_nodes(slist):
        if n.rand:
            print(f'{n.value} -> {n.rand.value}')
        else:
            print(f'{n.value} -> None')

@testwrapper
def test(arr):
    slist = new_slist(arr)
    make_rand(slist)
    print_rand(slist)
    s2 = complex_copy(slist)
    print('after copy:')
    print_rand(slist)
    print_rand(s2)

def main():
    test([3])
    test([3,9])
    test([3,5,1,7,2,6,9])

if __name__ == '__main__':
    main()
