#!/usr/bin/env python3
from collections import deque
import sys

from sodacomm.tools import testwrapper

def shortest_path(mx):
    R = len(mx)
    C = len(mx[0])
    visited = [[0] * C for i in range(R)]
    path = 0
    qu = deque()
    qu.append((0, 0))
    while qu:
        i, j = qu.popleft()
        path += 1
        visited[i][j] = 1
        if i == R-1 and j == C-1:
            return path
        if j > 0 and mx[i][j-1] == 1 and visited[i][j-1] == 0:
            qu.append((i, j-1))
        if i > 0 and mx[i-1][j] == 1 and visited[i-1][j] == 0:
            qu.append((i-1, j))
        if j < C-1 and mx[i][j+1] == 1 and visited[i][j+1] == 0:
            qu.append((i, j+1))
        if i < R-1 and mx[i+1][j] == 1 and visited[i+1][j] == 0:
            qu.append((i+1, j))

    return -1

@testwrapper
def test(mx):
    print(mx)
    print(shortest_path(mx))

def main():
    test([[1,0,1,1,1],[1,0,1,0,1],[1,1,1,0,1],[0,0,0,0,1]])
    test([[1,0,1,1,1],[1,0,0,0,1],[1,1,1,0,1],[0,0,0,0,1]])

if __name__ == '__main__':
    main()
