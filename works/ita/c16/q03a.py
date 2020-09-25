#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

class Heap:

    def __init__(self, hfm, capacity):
        self.hfm = hfm
        self.capacity = capacity
        self.h = [None] * (capacity + 1)
        self.size = 0

    def push(self, hix):
        self.size += 1
        self.h[self.size] = hix

        p = self.size
        while p > 1:
            s = p//2
            if self.hfm[self.h[s]].freq > self.hfm[self.h[p]].freq:
                t = self.h[s]
                self.h[s] = self.h[p]
                self.h[p] = t
            p = s

    def pop(self):
        if self.size == 0:
            return

        top = self.h[1]
        if self.size > 1:
            self.h[1] = self.h[self.size]
            self.adjust(1)

        self.size -= 1
        return top

    def adjust(self, p):
        while True:
            L = p << 1
            R = L + 1
            if L > self.size:
                break
            elif L == self.size:
                c = L
            else:
                if self.hfm[self.h[L]].freq < self.hfm[self.h[R]].freq:
                    c = L
                else:
                    c = R
            if self.hfm[self.h[p]].freq > self.hfm[self.h[c]].freq:
                t = self.h[p]
                self.h[p] = self.h[c]
                self.h[c] = t
                p = c
            else:
                break

    def empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

class HfmCell:
    def __init__(self, ch = '', freq = 0):
        self.ch = ch
        self.freq = freq
        self.parent = self.left = self.mid = self.right = -1

def show_tri_haffman(ch, freq):
    n = len(ch)
    num_nodes = n + n//2
    hfm = [None] * num_nodes
    heap = Heap(hfm, n)

    j = n//2
    for i in range(n//2, num_nodes):
        hfm[i] = HfmCell(ch[i-j], freq[i-j])
        heap.push(i)

    while j > 0:
        a = heap.pop()
        b = heap.pop()
        j -= 1
        if not heap.empty():
            c = heap.pop()
            cell = HfmCell('', hfm[a].freq + hfm[b].freq + hfm[c].freq)
            cell.left = a
            cell.mid = b
            cell.right = c
            hfm[a].parent = hfm[b].parent = hfm[c].parent = j
        else:
            cell = HfmCell('', hfm[a].freq + hfm[b].freq)
            cell.left = a
            cell.mid = b
            hfm[a].parent = hfm[b].parent = j
        hfm[j] = cell
        heap.push(j)

    for c, f in zip(ch, freq):
        print('{} {:.3f}'.format(c, f))
    stk = []
    p = 0
    while True:
        if hfm[p].left >= 0:
            stk.append('0')
            p = hfm[p].left
        elif hfm[p].mid >= 0:
            stk.append('1')
            p = hfm[p].mid
        elif hfm[p].right >= 0:
            stk.append('2')
            p = hfm[p].right
        else:
            if hfm[p].ch:
                print('{} -> {}'.format(hfm[p].ch, ''.join(stk)))
            q = p
            p = hfm[p].parent
            if p >= 0:
                stk.pop()
                if q == hfm[p].left:
                    hfm[p].left = -1
                elif q == hfm[p].mid:
                    hfm[p].mid = -1
                else:
                    hfm[p].right = -1
            else:
                break

def test(n):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(chars)
    ch = chars[0:n]

    freq = [random.randint(1,99) for i in range(n)]
    T = sum(freq)
    for i in range(n):
        freq[i] = freq[i] / T

    show_tri_haffman(ch, freq)
    print('------')

def main():
    '''推广赫夫曼算法，生成三进制编码'''
    test(5)
    test(10)
    test(21)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
