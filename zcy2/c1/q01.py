#!/usr/bin/env python3
import sys

class MinStack:

    def __init__(self):
        self.vstk = []
        self.mstk = []

    def push(self, v):
        self.vstk.append(v)
        if not self.mstk or v <= self.mstk[-1]:
            self.mstk.append(v)

    def pop(self):
        i = self.vstk.pop()
        if i == self.mstk[-1]:
            self.mstk.pop()
        return i

    def top(self):
        return self.vstk[-1]

    def empty(self):
        return not self.vstk

    def min(self):
        return self.mstk[-1]

def test(seq, stk):
    for i in seq:
        stk.push(i)
        print((i, stk.min()), end = ' ')
    print('')
    while not stk.empty():
        print((stk.top(), stk.min()), end = ' ')
        stk.pop()
    print('')
    print('----')

def main():
    test([9,4,3,8,5,2,1], MinStack())
    test([1,2,3,4,5], MinStack())
    test([5,4,3,2,1], MinStack())
    test([1,1,3,3,2,2], MinStack())
    test([4,4,3,3,1,1], MinStack())

if __name__ == '__main__':
    main()
