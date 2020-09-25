#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

MAX = 0x7fffffff
MIN = -0x7fffffff

class TNode:

    def __init__(self, arr, index):
        self.arr = arr
        self.index = index
        self.cur = 0

    def has_next(self):
        return self.cur < len(self.arr)

    def top(self):
        return self.arr[self.cur] if self.has_next() else MAX

    def pop(self):
        if self.has_next():
            v = self.arr[self.cur]
            self.cur += 1
            return v
        else:
            return MAX

def k_merge_sort_win(arrs):
    k = len(arrs)
    tree = [None] * 2 * k
    for i in range(k):
        tree[i+k] = TNode(arrs[i], i)

    # init winner tree
    for i in range(k-1, 0, -1):
        L = tree[i * 2]
        R = tree[i * 2 + 1]
        if L.top() < R.top():
            tree[i] = L
        else:
            tree[i] = R

    r = []
    while True:
        winner = tree[1]
        if winner.top() == MAX:
            break
        r.append(winner.top())
        winner.pop()
        adjust_winner_tree(tree, (winner.index + k)>>1)
    return r

def adjust_winner_tree(tree, p):
    while p > 0:
        L = tree[p*2]
        R = tree[p*2+1]
        if L.top() < R.top():
            tree[p] = L
        else:
            tree[p] = R
        p >>= 1

def k_merge_sort_lose(arrs):
    k = len(arrs)
    tree = [TNode([MIN], k)] * k
    
    # init loser tree
    for i in range(k):
        node = TNode(arrs[i], i)
        adjust_loser_tree(tree, (i+k)>>1, node)

    r = []
    while True:
        winner = tree[0]
        if winner.top() == MAX:
            break
        r.append(winner.top())
        winner.pop()
        adjust_loser_tree(tree, (winner.index + k)>>1, winner)
    return r

def adjust_loser_tree(tree, p, node):
    w = node
    while p > 0:
        if tree[p].top() < w.top():
            t = tree[p]
            tree[p] = w
            w = t
        p >>= 1
    tree[0] = w

def test(k):
    arrs = []
    for i in range(k):
        n = random.randint(6, 12)
        a = [random.randint(1, 100) for i in range(n)]
        a.sort()
        arrs.append(a)
        print('[{}] {}'.format(i, a))
    print(k_merge_sort_win(arrs))
    print(k_merge_sort_lose(arrs))
    print()

def main():
    '''分别用胜者树和败者树实现K路归并排序'''
    test(2)
    test(3)
    test(5)
    test(10)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
