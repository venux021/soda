#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from q20 import gen_arr

class HeapNode(object):

    def __init__(self, value, src):
        self.value = value
        self.src = src

class Heap(object):

    def __init__(self, limit):
        self.h = [None] * (limit + 1)
        self.size = 0

    def push(self, node):
        if self.size == len(self.h) - 1:
            return
        self.size += 1
        self.h[self.size] = node
        i = self.size
        while i > 1:
            p = i / 2
            if self.h[p].value < node.value:
                self.swap(i, p)
                i = p
            else:
                break

    def top(self):
        return self.h[1]

    def pop(self):
        self.h[1] = self.h[self.size]
        self.h[self.size] = None
        self.size -= 1
        i = 1
        while True:
            left = i * 2
            right = left + 1
            if left > self.size:
                break
            elif left == self.size:
                child = left
            else:
                if self.h[left].value > self.h[right].value:
                    child = left
                else:
                    child = right
            if self.h[i].value < self.h[child].value:
                self.swap(i, child)
                i = child
            else:
                break

    def swap(self, i, j):
        t = self.h[i]
        self.h[i] = self.h[j]
        self.h[j] = t

def topk(arrs, k):
    n = len(arrs)
    heap = Heap(n)

    for i, arr in enumerate(arrs):
        heap.push(HeapNode(arr[-1], i))
        del arr[-1]

    r = []
    while True:
        if heap.size == 0:
            break
        top = heap.top()
        i = top.src
        r.append(top.value)
        if len(r) == k:
            break
        heap.pop()
        if len(arrs[i]) > 0:
            heap.push(HeapNode(arrs[i][-1], i))
            del arrs[i][-1]

    return r

def test(arrs, k):
    print 'arrs: {}, k: {}'.format(arrs, k)
    print 'topk: {}'.format(topk(arrs, k))

def main():
    '''打印N个数组整体最大的Top K'''
    test([[-65, -4, 3, 31, 76, 98], [-100, -79, -58, -44, -3, -2, 53, 79, 96], [-95, -46, -26, 6, 11, 58, 62, 96]], 5)
    test(gen_arr(3), 5)
    test(gen_arr(5), 8)
    test(gen_arr(1), 3)
    test(gen_arr(3), 40)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
