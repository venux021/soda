#!/usr/bin/env python3
from collections import deque
import random
import sys

class StackQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, v):
        self.s2.append(v)

    def dequeue(self):
        if not self.s1:
            self._transfer()
        return self.s1.pop()

    def head(self):
        if not self.s1:
            self._transfer()
        return self.s1[-1]

    def _transfer(self):
        while self.s2:
            self.s1.append(self.s2.pop())

    def empty(self):
        return not self.s1 and not self.s2

def test(seq, qu):
    s = deque(seq)
    it = 0
    while s or not qu.empty():
        i = random.randint(1, 100)
        if i >= 50 and s:
            qu.enqueue(s.popleft())
        elif i < 50 and not qu.empty():
            print(qu.dequeue(), end = ' ')
        it += 1
    print(f'\niter {it} times')

def main():
    test([1,2,3,4,5,6,7,8,9], StackQueue())

if __name__ == '__main__':
    main()
