#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def max_square(mx):
    n = len(mx)
    down = [[0] * n for _ in range(n)]
    right = [[0] * n for _ in range(n)]
    if mx[n-1][n-1] == 1:
        down[n-1][n-1] = right[n-1][n-1] = 1
    for i in range(n-2, -1, -1):
        right[i][n-1] = mx[i][n-1]
        down[i][n-1] = (down[i+1][n-1] + 1) if mx[i][n-1] == 1 else 0
        down[n-1][i] = mx[n-1][i]
        right[n-1][i] = 0 if mx[n-1][i] == 0 else right[n-1][i+1] + 1

    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            down[i][j] = 0 if mx[i][j] == 0 else (down[i+1][j] + 1)
            right[i][j] = 0 if mx[i][j] == 0 else (right[i][j+1] + 1)

    max_len = 0
    for i in range(n):
        for j in range(n):
            k = min(down[i][j], right[i][j])
            for p in range(k, 0, -1):
                if down[i][j+p-1] >= p and right[i+p-1][j] >= p:
                    max_len = max(max_len, p)
                    break

    return max_len

@testwrapper
def test(mx):
    print(mx)
    print(max_square(mx))

def main():
    test([[0,1,1,1,1],[0,1,0,0,1],[0,1,0,0,1],[0,1,1,1,1],[0,1,0,1,1]])

if __name__ == '__main__':
    main()
