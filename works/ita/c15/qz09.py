#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

MAX = sys.maxsize

def split_plan(s, splits):
    n = len(s)
    m = len(splits)
    splits = splits[:]
    splits.append(n)
    splits.append(0)

    dp = [[0] * m for i in range(m)]
    cuts = [[-1] * m for i in range(m)]

    for i in range(m):
        dp[i][i] = splits[i+1] - splits[i-1]
        cuts[i][i] = i

    for L in range(2, m+1):
        for i in range(0, m-L+1):
            j = i + L - 1
            dp[i][j] = MAX
            length = splits[j+1] - splits[i-1]
            for k in range(i, j+1):
                v = length
                if k > i:
                    v += dp[i][k-1]
                if k < j:
                    v += dp[k+1][j]
#                dp[i][j] = min(v, dp[i][j])
                if v < dp[i][j]:
                    dp[i][j] = v
                    cuts[i][j] = k

    print('string:', s)
    print('splits:', splits[:-2])
    show_plan(cuts, 0, m-1, splits, s)
    print('total cost:', dp[0][m-1])
    print('--------')
#    print('plan:')

def show_plan(cuts, start, end, splits, s):
    if start > end:
        return

    p = cuts[start][end]
    i = splits[start-1]
    j = splits[end+1]
    k = splits[p]
    print('cost {}, pos {}, {} -> {} + {}'.format(j-i, splits[p], s[i:j], s[i:k], s[k:j]))

    show_plan(cuts, start, p-1, splits, s)
    show_plan(cuts, p+1, end, splits, s)

def test(n, splits):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    string = ''.join([random.choice(chars) for i in range(n)])
    split_plan(string, splits)

def main():
    '''字符串最佳拆分'''
    test(10, [4,7])
    test(20, [3,8,10])
    test(100, [5,13,27,36,55,76,89,92])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
