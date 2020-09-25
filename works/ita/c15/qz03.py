#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import functools
import math

def _cmp(p1, p2):
    if p1[0] < p2[0]:
        return -1
    elif p1[0] == p2[0]:
        return 0
    else:
        return 1

def show_path(points):
    points.sort(key = functools.cmp_to_key(_cmp))
    n = len(points)
    dp = [[0] * n for i in range(n)]
    path = [[-1] * n for i in range(n)]

    dp[1][0] = distance(points[1], points[0])

    for i in range(2, n):
        for j in range(0, i-1):
            dp[i][j] = dp[i-1][j] + distance(points[i], points[i-1])
            path[i][j] = i-1
        dp[i][i-1] = 0x7fffffff
        for k in range(0, i-1):
            dist = distance(points[i], points[k]) + dp[i-1][k]
            if dist < dp[i][i-1]:
                dp[i][i-1] = dist
                path[i][i-1] = k

    p = n-1
    step1 = []
    while p >= 0:
        step1.append(points[p])
        p = path[p][p-1]

    i = 0
    j = len(points) - 1
    step2 = []
    while j >= 0:
        if i >= len(step1) or points[j] != step1[i]:
            step2.append(points[j])
        else:
            i += 1
        j -= 1

    print(step2 + step1[::-1])
    print(dp[n-1][n-2] + distance(points[n-1], points[n-2]))

def distance(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return math.sqrt(a*a + b*b)

def test(points):
    show_path(points)

def main():
    '''双调欧几里得旅行商问题'''
    test([(0,0),(5,2),(6,5),(2,3),(7,1),(1,6),(8,4)])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
