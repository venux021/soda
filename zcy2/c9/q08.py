#!/usr/bin/env python3
import sys
import time

from sodacomm.tools import testwrapper

class Node:

    def __init__(self, value):
        self.update(value)

    def update(self, value):
        self.value = value
        self.ts = time.time()

class SetAllHash:

    def __init__(self):
        self.m = {}
        self.sall = Node(None)
        
    def get(self, key):
        if key in self.m:
            if self.m[key].ts >= self.sall.ts:
                return self.m[key].value
            else:
                return self.sall.value

    def put(self, key, value):
        if key not in self.m:
            self.m[key] = Node(value)
        else:
            self.m[key].update(value)

    def containsKey(self, key):
        return key in self.m

    def setAll(self, value):
        self.sall.update(value)

@testwrapper
def test():
    h = SetAllHash()
    h.put('a','aa')
    h.put('b','bb')
    h.put('c','cc')
    for k in 'abc':
        print(k, h.get(k))
    h.setAll('zz')
    for k in 'abc':
        print(k, h.get(k))
    h.put('a','AA')
    for k in 'abc':
        print(k, h.get(k))

def main():
    test()

if __name__ == '__main__':
    main()
