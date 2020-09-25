#!/usr/bin/env python3
from collections import deque
import sys

class Pet:

    def __init__(self, atype):
        self.atype = atype

    def getPetType(self):
        return self.atype

    def __str__(self):
        return f'<{self.atype}>'

class Dog(Pet):

    def __init__(self):
        super().__init__("dog")

class Cat(Pet):

    def __init__(self):
        super().__init__("cat")

class CDQueue:

    def __init__(self):
        self.qu = deque()
        self.ndog = self.ncat = 0

    def add(self, pet):
        self.qu.append(pet)
        if pet.getPetType() == 'cat':
            self.ncat += 1
        else:
            self.ndog += 1

    def pollAll(self):
        q = list(self.qu)
        self.qu.clear()
        self.ndog = self.ncat = 0
        return q

    def pollDog(self):
        dogs = []
        for _ in range(self.ndog + self.ncat):
            p = self.qu.popleft()
            if p.getPetType() == 'dog':
                dogs.append(p)
            else:
                self.qu.append(p)
        self.ndog = 0
        return dogs

    def pollCat(self):
        cats = []
        for _ in range(self.ndog + self.ncat):
            p = self.qu.popleft()
            if p.getPetType() == 'cat':
                cats.append(p)
            else:
                self.qu.append(p)
        self.ncat = 0
        return cats

    def isEmpty(self):
        return self.ncat + self.ndog == 0

    def isDogEmpty(self):
        return self.ndog == 0

    def isCatEmpty(self):
        return self.ncat == 0

def test(qu, pets):
    print(f'start, isEmpty {qu.isEmpty()}, isDogEmpty() {qu.isDogEmpty()}, isCatEmpty {qu.isCatEmpty()}')
    for p in pets:
        qu.add(p)
    print(f'add pets, isEmpty {qu.isEmpty()}, isDogEmpty() {qu.isDogEmpty()}, isCatEmpty {qu.isCatEmpty()}')
    _all = qu.pollAll()
    print(f'all: {[str(k) for k in _all]}')
    print(f'after pollAll, isEmpty {qu.isEmpty()}, isDogEmpty() {qu.isDogEmpty()}, isCatEmpty {qu.isCatEmpty()}')
    print('reset')
    for p in pets:
        qu.add(p)
    _dogs = qu.pollDog()
    print(f'dogs: {[str(k) for k in _dogs]}')
    print(f'after pollDog, isEmpty {qu.isEmpty()}, isDogEmpty() {qu.isDogEmpty()}, isCatEmpty {qu.isCatEmpty()}')
    cats = qu.pollCat()
    print(f'cats: {[str(k) for k in cats]}')
    print(f'after pollCat, isEmpty {qu.isEmpty()}, isDogEmpty() {qu.isDogEmpty()}, isCatEmpty {qu.isCatEmpty()}')

def main():
    test(CDQueue(), [Dog(), Cat(), Cat(), Cat(), Dog(), Dog(), Cat(), Dog(), Dog(), Cat(), Cat(), Cat()])

if __name__ == '__main__':
    main()
