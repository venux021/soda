#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from bitree import BNode, parse_bitree

def pre_order_seq(t):
    r = []
    pre_order(t, r)
    return r

def in_order_seq(t):
    r = []
    in_order(t, r)
    return r

def post_order_seq(t):
    r = []
    post_order(t, r)
    return r

def post_order(t, r):
    if t:
        post_order(t.left, r)
        post_order(t.right, r)
        r.append(str(t.value))

def in_order(t, r):
    if t:
        in_order(t.left, r)
        r.append(str(t.value))
        in_order(t.right, r)

def pre_order(t, r):
    if t:
        r.append(str(t.value))
        pre_order(t.left, r)
        pre_order(t.right, r)

def pre_order_seq_2(t):
    r = []
    p = t
    stack = []
    while stack or p:
        if p:
            r.append(str(p.value))
            stack.append(p)
            p = p.left
        else:
            n = stack.pop()
            p = n.right
    return r

def in_order_seq_2(t):
    r = []
    p = t
    stack = []
    while stack or p:
        if p:
            stack.append(p)
            p = p.left
        else:
            n = stack.pop()
            r.append(str(n.value))
            p = n.right
    return r

def post_order_seq_2(t):
    r = []
    p = t
    stack = []
    while stack or p:
        if p:
            stack.append([p, False])
            p = p.left
        else:
            n = stack.pop()
            if not n[1]:
                p = n[0].right
                n[1] = True
                stack.append(n)
            else:
                r.append(str(n[0].value))
    return r

def test(s):
    if isinstance(s, str):
        tree = parse_bitree(s)
    elif isinstance(s, BNode):
        tree = s
    print('pre order: ', ' '.join(pre_order_seq(tree)), '|', ' '.join(pre_order_seq_2(tree)))
    print('in order:  ', ' '.join(in_order_seq(tree)), '|', ' '.join(in_order_seq_2(tree)))
    print('post order:', ' '.join(post_order_seq(tree)), '|', ' '.join(post_order_seq_2(tree)))
    print('------')

def main():
    test(parse_bitree('A'))
    test(parse_bitree('A B'))
    test(parse_bitree('A B C'))
    test(parse_bitree('A ## C'))
    test(parse_bitree('A B C D E ## F'))
    test('A B ## C ## D ## E')
    test('A ## B ## C ## D ## E')
    test('A B ## ## C D')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
