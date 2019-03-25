#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def rotate_x(mx):
    n = len(mx)
    i = 0
    j = n - 1
    while i < j:
        for k in range(j-i):
            tmp = mx[i][i+k]
            mx[i][i+k] = mx[j-k][i]
            mx[j-k][i] = mx[j][j-k]
            mx[j][j-k] = mx[i+k][j]
            mx[i+k][j] = tmp
        i += 1
        j -= 1

@testwrapper
def test(mx):
    print(mx)
    rotate_x(mx)
    print(mx)

def main():
    test([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    test([[1,2,3],[4,5,6],[7,8,9]])
    test([[1,2],[3,4]])

if __name__ == '__main__':
    main()
