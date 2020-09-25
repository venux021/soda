#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

class TNode:

    def __init__(self, *, isroot = False, parent = None, char = None):
        self.children = {}
        self.isroot = isroot
        self.isterm = False
        self.parent = parent
        self.char = char

    @property
    def is_root(self):
        return self.isroot

    @property
    def is_term(self):
        return self.isterm

    @is_term.setter
    def is_term(self, b):
        self.isterm = b

class Trie:

    def __init__(self):
        self.root = TNode(isroot = True)

    def insert(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TNode(parent = p, char = c)
            p = p.children[c]
        p.is_term = True

    def delete(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                return
            p = p.children[c]
        while p != self.root:
            t = p.parent
            if p.children:
                break
            del t.children[p.char]
            p = t

    def search(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return True

    def prefix_number(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                return 0
            p = p.children[c]
        return self._count_term(p)

    def _count_term(self, p):
        n = 0
        if p.is_term:
            n = 1
        for d in p.children.values():
            n += self._count_term(d)
        return n

@testwrapper
def test(strs):
    tree = Trie()
    for s in strs:
        b = tree.search(s)
        tree.insert(s)
        a = tree.search(s)
        n = tree.prefix_number(s)
        print(f'{s}: before insert {b}, after intert {a}, prefix {n}')

    for s in strs:
        b = tree.search(s)
        tree.delete(s)
        a = tree.search(s)
        n = tree.prefix_number(s)
        print(f'{s}: before delete {b}, after delete {a}, prefix {n}')

def main():
    test(['abc', 'abcd', 'abd', 'b', 'bcd', 'efg', 'hik'])

if __name__ == '__main__':
    main()
