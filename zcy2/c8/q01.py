#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def print_circular(mx):
    R = len(mx)
    C = len(mx[0])
    r1, r2 = 0, R-1
    c1, c2 = 0, C-1
    while r1 < r2 and c1 < c2:
        for i in range(c1, c2):
            print(mx[r1][i], end = ' ')
        for i in range(r1, r2):
            print(mx[i][c2], end = ' ')
        for i in range(c2, c1, -1):
            print(mx[r2][i], end = ' ')
        for i in range(r2, r1, -1):
            print(mx[i][c1], end = ' ')
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    if r1 == r2 and c1 == c2:
        print(mx[r1][c1], end = ' ')
    elif r1 == r2:
        for i in range(c1, c2+1):
            print(mx[r1][i], end = ' ')
    elif c1 == c2:
        for i in range(r1, r2+1):
            print(mx[i][c1], end = ' ')
    print('')

@testwrapper
def test(mx):
    print(mx)
    print_circular(mx)

def main():
    test([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    test([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    test([[1,2,3,4],[5,6,7,8]])
    test([[1,2,3,4]])
    test([[1],[2],[3],[4]])
    test([[1,2],[3,4],[5,6],[7,8]])
    test([[1,2,3],[4,5,6],[7,8,9]])

if __name__ == '__main__':
    main()
