#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class Node(object):

    def __init__(self):
        self.down = 0
        self.right = 0

def max_edge(m):
    n = len(m[0])
    nx = [[Node() for i in range(n)] for i in range(n)]

    for i in range(n):
        c = 0
        for j in range(n-1, -1, -1):
            if m[i][j] == 1:
                c += 1
                nx[i][j].right = c
            else:
                c = 0

    for j in range(n):
        c = 0
        for i in range(n-1, -1, -1):
            if m[i][j] == 1:
                c += 1
                nx[i][j].down = c
            else:
                c = 0

    Max = 0
    for i in range(n):
        for j in range(n):
            max_e = min(n-i, n-j)
            for k in range(max_e, Max, -1):
                if (nx[i][j].right >= k and nx[i][j].down >= k
                        and nx[i][j+k-1].down >= k
                        and nx[i+k-1][j].right >= k):
                    Max = max(Max, k)
                    break

    return Max

def test(m):
    print 'm: {}'.format(m)
    print 'edge: {}'.format(max_edge(m))

def main():
    '''边界都是1的最大正方形大小'''
    test([[0,1,1,1,1],[0,1,0,0,1],[0,1,0,0,1],[0,1,1,1,1],[0,1,0,1,1]])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
