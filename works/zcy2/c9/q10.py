#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Cache:

    def __init__(self, capa):
        self.capacity = capa
        self.size = 0
        self.m = {}
        self.head = None
        self.tail = None

    def set(self, key, value):
        if key not in self.m:
            node = Node(value)
            self.m[key] = node
            if not self.head:
                self.head = self.tail = self.m[key]
            else:
                self.head.prev = node
                node.next = self.head
                self.head = node
            self.size += 1
            if self.size > self.capacity:
                t = self.tail
                self.tail = t.prev
                t.prev = None
                if self.tail:
                    self.tail.next = None
                else:
                    self.head = None
                self.size -= 1
        else:
            node = self.m[key]
            node.value = value
            self._make_most_use(key)

    def _make_most_use(self, key):
        node = self.m[key]
        if node == self.tail:
            self.tail = node.prev
        _prev = node.prev
        _next = node.next
        if _prev:
            _prev.next = _next
        if _next:
            _next.prev = _prev
        node.prev = None
        self.head.prev = node
        node.next = self.head
        self.head = node

    def get(self, key):
        if key in self.m:
            self._make_most_use(key)
            return self.m[key].value

    def least_use(self):
        if self.tail:
            return self.tail.value

    def most_use(self):
        if self.head:
            return self.head.value

@testwrapper
def test():
    ch = Cache(3)
    ch.set('A', 1)
    print(f'most use: {ch.most_use()}')
    ch.set('B', 2)
    print(f'most use: {ch.most_use()}')
    print(f'least use: {ch.least_use()}')
    ch.set('C', 3)
    print(f'most use: {ch.most_use()}')
    print(f'least use: {ch.least_use()}')
    print(f'value of \'A\': {ch.get("A")}')
    print(f'most use: {ch.most_use()}')
    print(f'least use: {ch.least_use()}')
    ch.set('D', 4)
    print(f'most use: {ch.most_use()}')
    print(f'least use: {ch.least_use()}')

def main():
    test()

if __name__ == '__main__':
    main()
