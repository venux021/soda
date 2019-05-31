#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def spiral_print(mx):
    R = len(mx)
    C = len(mx[0])
    r1, c1 = 0, 0
    r2, c2 = R-1, C-1
    seq = []
    while r1 <= r2 and c1 <= c2:
        output(mx, r1, c1, r2, c2, seq)
        r1 += 1
        c1 += 1
        r2 -= 1
        c2 -= 1
    return seq

def output(mx, r1, c1, r2, c2, seq):
    if r1 == r2:
        for i in range(c1, c2+1):
            seq.append(mx[r1][i])
    elif c1 == c2:
        for i in range(r1, r2+1):
            seq.append(mx[i][c1])
    else:
        r = r1
        c = c1
        while c < c2:
            seq.append(mx[r][c])
            c += 1
        while r < r2:
            seq.append(mx[r][c])
            r += 1
        while c > c1:
            seq.append(mx[r][c])
            c -= 1
        while r > r1:
            seq.append(mx[r][c])
            r -= 1

@testwrapper
def test(mx):
    print(mx)
    print(spiral_print(mx))

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
