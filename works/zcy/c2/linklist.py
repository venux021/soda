# -*- coding: utf-8 -*-

class ListNode:

    def __init__(self, value = None):
        self.value = value
        self.next = self.prev = None

    def str_val(self):
        return str(self.value)


def parse_list(s, value_conv = None, split = ' ', with_head = False):
    if not s:
        return None

    if not value_conv:
        value_conv = lambda x: x

    head = tail = ListNode()
    for d in s.split(split):
        n = ListNode(value_conv(d))
        tail.next = n
        n.prev = tail
        tail = n

    if not with_head:
        head = head.next
        head.prev = None

    return head

def show_list(L, prompt = None):
    if prompt:
        print(prompt, '', end='')

    if not L:
        print('[]')
        return
    elif L.value is None:
        L = L.next

    print('[', end='')
    while L:
        print(L.str_val(), '', end = '')
        L = L.next
    print(']')

def reverse_list(L):
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

