#!/usr/bin/env python3
import sys
import time

from sodacomm.bitree import *
from sodacomm.tools import testwrapper

def pre_order_1(t):
    if not t:
        return
    stk = []
    p = t
    while p or stk:
        while p:
            print(p.value, end = ' ')
            stk.append(p)
            p = p.lc
        if stk:
            top = stk.pop()
            p = top.rc
    print('')

def pre_order_2(t):
    if not t:
        return
    stk = [t]
    while stk:
        top = stk.pop()
        print(top.value, end = ' ')
        if top.rc:
            stk.append(top.rc)
        if top.lc:
            stk.append(top.lc)
    print('')

def in_order(t):
    if not t:
        return
    stk = []
    p = t
    while p or stk:
        while p:
            stk.append(p)
            p = p.lc
        if stk:
            top = stk.pop()
            print(top.value, end = ' ')
            p = top.rc
    print('')

def post_order_1(t):
    if not t:
        return
    stk = []
    p = t
    last = None
    while p or stk:
        while p:
            stk.append(p)
            p = p.lc
        top = stk[-1]
        if not top.lc and not top.rc or last == top.rc or last == top.lc and not top.rc:
            print(top.value, end = ' ')
            last = top
            stk.pop()
        else:
            p = top.rc
    print('')

def post_order_2(t):
    if not t:
        return
    stk = [t]
    pre = Node()
    while stk:
        top = stk[-1]
        if top.lc and pre != top.lc and pre != top.rc:
            stk.append(top.lc)
        elif top.rc and pre != top.rc:
            stk.append(top.rc)
        else:
            stk.pop()
            print(top.value, end = ' ')
            pre = top
    print('')

def post_order_3(t):
    if not t:
        return
    s1 = [t]
    s2 = []
    while s1:
        top = s1.pop()
        if top.lc:
            s1.append(top.lc)
        if top.rc:
            s1.append(top.rc)
        s2.append(top)
    while s2:
        top = s2.pop()
        print(top.value, end = ' ')
    print('')

@testwrapper
def test(arr):
    tree = new_bitree_level(arr)
    print_tree(tree)
    pre_order_1(tree)
    pre_order_2(tree)
    in_order(tree)
    post_order_1(tree)
    post_order_2(tree)
    post_order_3(tree)

def main():
    test([1,2,3,4,5,None,6])
    test([1,2,3,4,None,None,6])
    test([1,2,3,None,4,5,6])

if __name__ == '__main__':
    main()
