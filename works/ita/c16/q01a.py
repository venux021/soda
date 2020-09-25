#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def show_optimal_actions(actions):
    first = (actions[0][0]-1, actions[0][0]-1)
    last = (actions[-1][1]+1, actions[-1][1]+1)
    ats = [first] + actions + [last]
    n = len(ats)
    dp = [[0] * n for i in range(n)]
    path = [[-1] * n for i in range(n)]

    for L in range(3, n+1):
        for i in range(0, n-L+1):
            j = i + L - 1
            for k in range(i+1, j):
                if is_cmpt(ats[i], ats[k]) and is_cmpt(ats[k], ats[j]):
                    D = dp[i][k] + dp[k][j] + 1
                    if D > dp[i][j]:
                        dp[i][j] = D
                        path[i][j] = k

    print('count:', dp[0][n-1])
    print('actions:', list(map(lambda x: ats[x], collect_action(ats, path))))

def collect_action(actions, path):
    selected = []
    _ca(actions, path, 0, len(actions)-1, selected)
    return selected

def _ca(actions, path, i, j, selected):
    if path[i][j] < 0:
        return

    k = path[i][j]
    selected.append(k)
    _ca(actions, path, i, k, selected)
    _ca(actions, path, k, j, selected)

def is_cmpt(a, b):
    return b[0] >= a[1] or a[0] >= b[1]

def test(actions):
    show_optimal_actions(actions)

def main():
    '''动态规划解活动选择问题'''
    test([(1,4),(3,5),(0,6),(5,7),(3,9),
            (5,9),(6,10),(8,11),(8,12),(2,14),(12,16)])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
