#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def find_half(arr):
    n = len(arr)
    t = 0
    c = None
    for i in arr:
        if t == 0:
            t += 1
            c = i
        elif i == c:
            t += 1
        else:
            t -= 1
    t = 0
    for i in arr:
        if c == i:
            t += 1
    if t > n//2:
        return c

class Counter:

    def __init__(self, n):
        self.n = n
        self.values = [None] * n
        self.counts = [0] * n
        self.p = 0

    def count(self, v):
        for i in range(self.p):
            if self.values[i] == v:
                self.counts[i] += 1
                return
        if self.p < self.n:
            self.counts[self.p] = 1
            self.values[self.p] = v
            self.p += 1
        else:
            for i in range(self.p):
                self.counts[i] -= 1
            i = 0
            while i < self.p:
                if self.counts[i] == 0:
                    self.counts[i] = self.counts[self.p-1]
                    self.values[i] = self.values[self.p-1]
                    self.p -= 1
                else:
                    i += 1

    def get_values(self):
        return self.values[:self.p]

    def get_value_counts(self):
        return [(self.values[i], self.counts[i]) for i in range(self.p)]

def find_nk(arr, k):
    ctn = Counter(k-1)
    for v in arr:
        ctn.count(v)

    values = ctn.get_values()
    ctn = Counter(len(values))
    for v in arr:
        if v in values:
            ctn.count(v)

    vc = ctn.get_value_counts()
    results = []
    n = len(arr)
    for v, c in vc:
        if c > n//k:
            results.append(v)
    return results

@testwrapper
def test(arr):
    print(arr)
    print(find_half(arr))

@testwrapper
def test2(arr, k):
    print(arr, k)
    print(find_nk(arr, k))

def main():
    test2([1,1,2,2,3,3,3,5], 4)
    test2([1,1,1,2,3,3,3,5], 4)
    test2([2,2,2,2,2,2,2,2], 4)
    test2([1,2,3,4,5,6,7,8], 4)
    test([1,3,1,1,1,5,1,6,1,9])
    test([1,3,1,4,1,1,1,6,8])
    test([1,3,1,4,1,5,1,6])
    test([1,2,3,4,4,3,2,1])

if __name__ == '__main__':
    main()
