#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class Node(object):

    def __init__(self, i, j, s):
        self.i = i
        self.j = j
        self.s = s

def top_k(a1, a2, k):
    m = len(a1)
    n = len(a2)
    mx = [[0] * n for i in range(m)]
    heap = [None] * (m*n)
    heap_size = 0

    heap[1] = Node(m-1, n-1, a1[m-1] + a2[n-1])
    heap_size = 1
    mx[m-1][n-1] = 1

    result = []
    while len(result) < k and heap_size > 0:
        result.append(heap[1].s)
        ch = heap[1]
        if heap_size > 1:
            heap[1] = heap[heap_size]
            heap[heap_size] = None
            adjust_heap(heap, heap_size - 1)
        else:
            heap[1] = None
        heap_size -= 1

        if ch.i > 0 and mx[ch.i-1][ch.j] == 0:
            heap_size += 1
            heap[heap_size] = Node(ch.i-1, ch.j, a1[ch.i-1] + a2[ch.j])
            push_heap(heap, heap_size)
            mx[ch.i-1][ch.j] = 1
        if ch.j > 0 and mx[ch.i][ch.j-1] == 0:
            heap_size += 1
            heap[heap_size] = Node(ch.i, ch.j-1, a1[ch.i] + a2[ch.j-1])
            push_heap(heap, heap_size)
            mx[ch.i][ch.j-1] = 1

    return result


def dump_heap(h, size):
    strs = []
    for i in range(1, size+1):
        strs.append('{},{},{}'.format(h[i].i, h[i].j, h[i].s))
    print ' '.join(strs)


def push_heap(h, size):
    i = size
    while i > 1:
        p = i / 2
        if h[i].s > h[p].s:
            temp = h[i]
            h[i] = h[p]
            h[p] = temp
            i = p
        else:
            break


def adjust_heap(h, size):
    i = 1
    while True:
        left = i * 2
        right = left + 1
        if left > size:
            break
        elif left == size:
            t = left
        else:
            t = left if h[left].s >= h[right].s else right
        
        if h[i].s < h[t].s:
            temp = h[i]
            h[i] = h[t]
            h[t] = temp
            i = t
        else:
            break
            
    

def test(a1, a2, k):
    print 'a1: {}, a2: {}, k: {}'.format(a1, a2, k)
    print 'top k: {}'.format(top_k(a1, a2, k))

def main():
    '''两个有序数组间相加和的top k问题'''
    test([1,2,3,4,5], [3,5,7,9,11], 4)
    test([1,2,3,4,5], [3,5,7,9,11], 25)
    test([1,2,3,4,5], [3,5,7,9,11], 30)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()

