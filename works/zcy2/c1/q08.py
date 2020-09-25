#!/usr/bin/env python3
import sys

class Node:

    def __init__(self, value):
        self.value = value
        self.left = self.right = None

def build_max_tree(arr):
    if not arr:
        return
    n = len(arr)
    Lstk = []
    Lv = [None] * n
    Rstk = []
    Rv = [None] * n
    nodes = {v: Node(v) for v in arr}
    for i in range(len(arr)):
        while Lstk and Lstk[-1] < arr[i]:
            Lstk.pop()
        if Lstk:
            Lv[i] = Lstk[-1]
        Lstk.append(arr[i])
    for i in range(n-1, -1, -1):
        while Rstk and Rstk[-1] < arr[i]:
            Rstk.pop()
        if Rstk:
            Rv[i] = Rstk[-1]
        Rstk.append(arr[i])
    root = None
    for i in range(n):
        node = nodes[arr[i]]
        if Lv[i] is not None and Rv[i] is not None:
            if Lv[i] < Rv[i]:
                set_child(nodes[Lv[i]], node)
            else:
                set_child(nodes[Rv[i]], node)
        elif Lv[i] is not None:
            set_child(nodes[Lv[i]], node)
        elif Rv[i] is not None:
            set_child(nodes[Rv[i]], node)
        else:
            root = node
    return root

def set_child(parent, child):
    if not parent.left:
        parent.left = child
    elif not parent.right:
        parent.right = child

def show_tree(root):
    def _pre(r):
        if r:
            print(r.value, end = ' ')
            _pre(r.left)
            _pre(r.right)
    def _in(r):
        if r:
            _in(r.left)
            print(r.value, end = ' ')
            _in(r.right)
    _pre(root)
    print('')
    _in(root)
    print('')

def test(arr):
    tree = build_max_tree(arr)
    print(arr)
    show_tree(tree)

def main():
    test([3,4,5,1,2])

if __name__ == '__main__':
    main()
