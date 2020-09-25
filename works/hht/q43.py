#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def get_points(n):
    max_points = n * 6
    dp = [0] * (max_points + 1)

    for i in range(1,7):
        dp[i] = 1

    min_p = 1
    max_p = 6
    for i in range(2, n+1):
        next_min_p = i
        next_max_p = i * 6
        for j in range(next_max_p, next_min_p-1, -1):
            dp[j] = 0
            for k in range(max(j-6,min_p), min(max_p, j-1)+1):
                dp[j] += dp[k]
        min_p = next_min_p
        max_p = next_max_p       

    r = []
    for i in range(min_p, max_p + 1):
        r.append((i, dp[i]))
    return r

def test(n):
    print('n: {}'.format(n))
    print('points: {}'.format(get_points(n)))

def main():
    '''n个骰子的点数'''
    test(1)
    test(2)
    test(3)
    test(4)
    test(10)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
