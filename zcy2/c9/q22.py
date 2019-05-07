#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

class Section:

    def __init__(self, _min, _max):
        self.min = _min
        self.max = _max

class MessageBox:

    def __init__(self):
        self.expect = 1
        self.sect = {}

    def add(self, num):
        self.insert(num)
        if num == self.expect:
            s = self.dump_sect(num)
            self.expect = s[-1] + 1
            return s
        else:
            return []

    def dump_sect(self, num):
        s = self.sect[num]
        a = s.min
        b = s.max
        self.sect.pop(a,None)
        self.sect.pop(b,None)
        return [i for i in range(a, b+1)]

    def insert(self, num):
        s = Section(num, num)
        self.sect[num] = s
        if num-1 in self.sect:
            self.merge(num-1, num)
        if num+1 in self.sect:
            self.merge(num, num+1)

    def merge(self, a, b):
        if a > b:
            a, b = b, a
        left = self.sect[a]
        right = self.sect[b]
        if left.max + 1 != right.min:
            return
        left.max = right.max
        self.sect.pop(right.min, None)
        self.sect.pop(left.max, None)
        self.sect[right.max] = left

class MessageBuffer:

    def __init__(self):
        self.expect = 1
        self.heap = [None]
        self.size = 0

    def add(self, num):
        if num == self.expect:
            buf = [num]
            self.expect += 1
            self.dump(buf)
            return buf
        else:
            self.push_heap(num)
            return []

    def heap_top(self):
        return self.heap[1]

    def pop_heap(self):
        v = self.heap_top()
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        i = 1
        while i <= self.size // 2:
            L = i * 2
            R = L + 1
            if R > self.size or self.heap[L] <= self.heap[R]:
                T = L
            else:
                T = R
            if self.heap[i] > self.heap[T]:
                self.heap[i], self.heap[T] = self.heap[T], self.heap[i]
            else:
                break
            i = T
        return v

    def dump(self, buf):
        while self.size > 0 and self.heap_top() == self.expect:
            buf.append(self.pop_heap())
            self.expect += 1

    def push_heap(self, num):
        if len(self.heap) == self.size + 1:
            self.heap.append(num)
        else:
            self.heap[self.size+1] = num
        self.size += 1
        i = self.size
        while i > 1:
            parent = i // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            else:
                break
            i = parent

@testwrapper
def test(seq):
    print(seq)
    mb = MessageBuffer()
    for i in seq:
        r = mb.add(i)
        print(i, r)
    print('~~~~')
    mx = MessageBox()
    for i in seq:
        r = mx.add(i)
        print(i, r)

def main():
    test([2,1,4,5,7,3,9,8,6])

if __name__ == '__main__':
    main()
