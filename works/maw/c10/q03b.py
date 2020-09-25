#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import functools

def show_optimal_search_tree(words):
    words.sort(key = lambda x: x[0])
    print(words)
    n = len(words)
    cost = [[0] * n for i in range(n)]
    dp = [[0] * n for i in range(n)]
    loc = [[-1] * n for i in range(n)]
    for i in range(n):
        dp[i][i] = cost[i][i] = words[i][1]
        loc[i][i] = i

    for L in range(2, n+1):
        for i in range(0, n-L+1):
            j = i + L - 1
            C = 0
            dp[i][j] = 0x7fffffff
            for k in range(i, j+1):
                C += words[k][1]
                left = (dp[i][k-1] + cost[i][k-1]) if k > i else 0
                right = (dp[k+1][j] + cost[k+1][j]) if k < j else 0
                z = words[k][1] + left + right
                if z < dp[i][j]:
                    dp[i][j] = z
                    loc[i][j] = k
            cost[i][j] = C

    show_in_tree(0, n-1, loc, words)
    print('\ntotal:', dp[0][n-1])

def show_in_tree(i, j, loc, words):
    if i == j:
        print(words[i][0], end = '')
        return
    elif i > j:
        return

    k = loc[i][j]
    print(words[k][0], end = '')

    print('(', end = '')
    show_in_tree(i, k-1, loc, words)
    print(',', end = '')
    show_in_tree(k+1, j, loc, words)
    print(')', end = '')

def test(words):
    show_optimal_search_tree(words)

def main():
    '''最优二叉查找树'''
    test([('a',0.22),('am',0.18),('and',0.2),('egg',0.05),
            ('if',0.25),('the',0.02),('two',0.08)])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
