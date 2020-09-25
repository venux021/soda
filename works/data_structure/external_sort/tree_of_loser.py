#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

class InputSource:

    def __init__(self, *iterables):
        self.sources = iterables[:]
        self.count = len(self.sources)
        self.iters = [iter(s) for s in self.sources]
        self.values = [0] * self.count
        for i in range(self.count):
            self.next(i)

    def next(self, i):
        if i < 0 or i >= self.count:
            return -sys.maxsize
        try:
            v = next(self.iters[i])
        except StopIteration:
            v = sys.maxsize

        self.values[i] = v
        return v

    def current(self, i):
        if i < 0 or i >= self.count:
            return -sys.maxsize
        return self.values[i]

class TreeOfLoser:

    def __init__(self, *iterables):
        self.input_source = InputSource(*iterables)
        self.N = self.input_source.count
        self.tree = [self.N] * self.N
        self.initialize()

    def initialize(self):
#        for i in range(self.N-1, -1, -1):
        for i in range(self.N):
            self.adjust(i)

    def adjust(self, i):
        t = (i + self.N) // 2
        while t > 0:
            if self.input_source.current(i) > self.input_source.current(self.tree[t]):
                self.tree[t], i = i, self.tree[t]
            t //= 2
        self.tree[0] = i

    def pop(self):
        i = self.tree[0]
        v = self.input_source.current(i)
        self.input_source.next(i)
        self.adjust(i)
        return v

@testwrapper
def test(*arrs):
    for a in arrs:
        print(a)
    tor = TreeOfLoser(*arrs)
    while True:
        v = tor.pop()
        if v == sys.maxsize:
            break
        print(v, end = ' ')
    print('')

def main():
    test([1,3,5,7,9], [2,4,9,13,24], [1,2,3,4,5,6,7,8,9,10], [-3,-2,-1,2,9,13], [-1,3,6,11,17,25,33,40])

if __name__ == '__main__':
    main()
