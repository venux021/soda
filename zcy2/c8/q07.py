#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def find_in_matrix(mx, v):
    R = len(mx)
    C = len(mx[0])
    i = 0
    j = C - 1
    while i < R and j >= 0:
        if v < mx[i][j]:
            j -= 1
        elif v > mx[i][j]:
            i += 1
        else:
            return True
    return False

@testwrapper
def test(mx, v):
    print(mx, v)
    print(find_in_matrix(mx, v))

def main():
    test([[0,1,2,5],[2,3,4,7],[4,4,4,8],[5,7,7,9]], 7)
    test([[0,1,2,5],[2,3,4,7],[4,4,4,8],[5,7,7,9]], 6)

if __name__ == '__main__':
    main()
