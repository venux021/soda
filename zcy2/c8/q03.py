#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def zigzag(mx):
    R = len(mx)
    C = len(mx[0])
    r1, c1, r2, c2 = 0, 0, 0, 0
    print(mx[0][0], end = ' ')
    if R == C and R == 1:
        print('')
        return
    def next1(a, b):
        if b < C - 1:
            return (a, b+1)
        elif a < R - 1:
            return (a+1, b)
        else:
            return (a, b)
    def next2(a, b):
        if a < R - 1:
            return (a+1, b)
        elif b < C - 1:
            return (a, b+1)
        else:
            return (a, b)
    r1, c1 = next1(r1, c1)
    r2, c2 = next2(r2, c2)
    up = False
    while r1 != r2 or c1 != c2:
        if up:
            i, j = r2, c2
            while i >= r1 and j <= c1:
                print(mx[i][j], end = ' ')
                i -= 1
                j += 1
        else:
            i, j = r1, c1
            while i <= r2 and j >= c2:
                print(mx[i][j], end = ' ')
                i += 1
                j -= 1
        r1, c1 = next1(r1, c1)
        r2, c2 = next2(r2, c2)
        up = not up
    print(mx[r1][c1])

@testwrapper
def test(mx):
    print(mx)
    zigzag(mx)

def main():
    test([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
    test([[1,2],[3,4]])
    test([[1,2],[3,4],[5,6]])

if __name__ == '__main__':
    main()
