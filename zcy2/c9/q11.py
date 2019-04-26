#!/usr/bin/env python3
import random
import sys

from sodacomm.tools import testwrapper

class RandomPool:

    def __init__(self):
        self.pool = []
        self.map = {}

    @property
    def size(self):
        return len(self.pool)

    def insert(self, key):
        if key not in self.map:
            self.map[key] = self.size
            self.pool.append(key)

    def delete(self, key):
        if key not in self.map:
            return
        loc = self.map[key]
        if loc < self.size - 1:
            self.pool[loc] = self.pool[-1]
            self.map[self.pool[-1]] = loc
        self.map.pop(key)
        self.pool.pop()

    def getRandom(self):
        return self.pool[int(random.random() * self.size)]

@testwrapper
def test():
    rp = RandomPool()
    rp.insert(1)
    rp.insert(2)
    rp.insert(3)
    rp.delete(1)
    print(rp.getRandom())
    print(rp.getRandom())
    print(rp.getRandom())

def main():
    test()

if __name__ == '__main__':
    main()
