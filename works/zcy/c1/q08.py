#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('../..')

from zcy.c3 import bitree

def max_tree(arr):
    n = len(arr)
    left_first = [None] * n
    right_first = [None] * n

    stk = []
    for i in range(n):
        while stk and stk[-1] < arr[i]:
            stk.pop()
        if stk:
            left_first[i] = stk[-1]
        stk.append(arr[i])

    stk = []
    for i in range(n-1, -1, -1):
        while stk and stk[-1] < arr[i]:
            stk.pop()
        if stk:
            right_first[i] = stk[-1]
        stk.append(arr[i])

    nmap = {}
    for v in arr:
        nmap[v] = bitree.BNode(v)

    head = None
    for i in range(n):
        v = arr[i]
        left = left_first[i]
        right = right_first[i]

        if left is not None:
            left = nmap[left]
        if right is not None:
            right = nmap[right]

        if left is None and right is None:
            head = nmap[v]
        elif left is None:
            if not right.left:
                right.left = nmap[v]
            else:
                right.right = nmap[v]
        elif right is None:
            if not left.left:
                left.left = nmap[v]
            else:
                left.right = nmap[v]
        else:
            if left.value < right.value:
                parent = left
            else:
                parent = right
            if not parent.left:
                parent.left = nmap[v]
            else:
                parent.right = nmap[v]

    return head

def test(arr):
    tree = max_tree(arr)
    print(arr)
    bitree.level_print(tree)
    print('----')

def main():
    '''构造数组的MaxTree'''
    test([3,4,5,1,2])
    test([3,4])
    test([3])
    test([3,6,4,2,7,1,9,8,5])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
