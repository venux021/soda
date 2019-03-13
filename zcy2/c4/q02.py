#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def min_path_sum(mx):
    row = len(mx)
    col = len(mx[0])
    s = [[0] * col for _ in range(row)]
    s[row-1][col-1] = mx[row-1][col-1]
    for i in range(row-1, -1, -1):
        for j in range(col-1, -1, -1):
            right = j + 1
            if right < col:
                r = mx[i][j] + s[i][right]
            else:
                r = sys.maxsize
            down = i + 1
            if down < row:
                d = mx[i][j] + s[down][j]
            else:
                d = sys.maxsize
            v = min(r, d)
            if v < sys.maxsize:
                s[i][j] = v
    return s[0][0]

@testwrapper
def test(mx):
    print(mx)
    s = min_path_sum(mx)
    print(s)

def main():
    test([[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]])

if __name__ == '__main__':
    main()
