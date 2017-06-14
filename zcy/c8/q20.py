#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys

class hnode(object):

    def __init__(self, arr):
        self.arr = arr
        self.index = len(arr) - 1

    def value(self):
        return self.arr[self.index]

def topk(arrs, k):
    n = len(arrs)
    heap = [None] * (n+1)
    for i in range(n):
        heap[i+1] = hnode(arrs[i])

    heapify(heap)

    tk = []
    for i in range(k):
        h = heap[1]
        tk.append(h.value())
        if h.index == 0:
            heap[1] = heap[-1]
            del heap[-1]
        else:
            h.index -= 1
        adjust_heap(heap)

    return tk

def dump_heap(heap):
    print 'heap: {}'.format([heap[i].value() for i in range(1, len(heap))])

def heapify(heap):
    n = len(heap)-1
    for i in range(n/2, 0, -1):
        s = i
        while s <= n/2:
            left = s * 2
            right = left + 1
            if right > n or heap[left].value() >= heap[right].value():
                t = left
            else:
                t = right
            if heap[t].value() > heap[s].value():
                tmp = heap[t]
                heap[t] = heap[s]
                heap[s] = tmp
                s = t
            else:
                break


def adjust_heap(heap):
    n = len(heap)-1
    s = 1
    while s <= n/2:
        left = s * 2
        right = left + 1
        if right > n or heap[left].value() >= heap[right].value():
            t = left
        else:
            t = right
        if heap[t].value > heap[s].value():
            tmp = heap[t]
            heap[t] = heap[s]
            heap[s] = tmp
            s = t
        else:
            break

def gen_arr(n):
    arrs = []
    for i in range(n):
        L = random.randint(5,10)
        a = [random.randint(-100,100) for j in range(L)]
        a.sort()
        arrs.append(a)
    return arrs

def test(arrs, k):
    print 'arrs: {}, k: {}'.format(arrs, k)
    print 'topk: {}'.format(topk(arrs, k))

def main():
    '''打印N个数组整体最大的top K'''
    test([[-65, -4, 3, 31, 76, 98], [-100, -79, -58, -44, -3, -2, 53, 79, 96], [-95, -46, -26, 6, 11, 58, 62, 96]], 5)
    test(gen_arr(3), 5)
    test(gen_arr(5), 8)
    test(gen_arr(1), 3)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
