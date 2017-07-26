#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

MAX = sys.maxsize

def align_plan(d1, d2, copy, replace, insert, delete):
    m = len(d1)
    n = len(d2)
    d1 = [''] + list(d1)
    d2 = [''] + list(d2)

    dp = [[0] * (n+1) for i in range(m+1)]
    action = [[None] * (n+1) for i in range(m+1)]
    for i in range(1, n+1):
        dp[0][i] = dp[0][i-1] + insert
        action[0][i] = 'I'
    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] + delete
        action[i][0] = 'D'

    for i in range(1, m+1):
        for j in range(1, n+1):
            c_replace = dp[i-1][j-1] + replace
            dp[i][j] = c_replace
            action[i][j] = 'R'

            c_insert = dp[i][j-1] + insert
            if c_insert < dp[i][j]:
                dp[i][j] = c_insert
                action[i][j] = 'I'

            c_delete = dp[i-1][j] + delete
            if c_delete < dp[i][j]:
                dp[i][j] = c_delete
                action[i][j] = 'D'

            if d1[i] == d2[j]:
                c_copy = dp[i-1][j-1] + copy
                if c_copy < dp[i][j]:
                    dp[i][j] = c_copy
                    action[i][j] = 'C'

    acts = []
    i = m
    j = n
    while i > 0 or j > 0:
        a = action[i][j]
        acts.append(a)
        if a == 'C' or a == 'R':
            i -= 1
            j -= 1
        elif a == 'I':
            j -= 1
        else:
            i -= 1

    acts = acts[::-1]

    i = j = 1
    k1 = []
    k2 = []
    k3 = []

    for a in acts:
        if a == 'I':
            k1.append(' ')
            k2.append(d2[j])
            j += 1
            k3.append('*')
        elif a == 'D':
            k1.append(d1[i])
            i += 1
            k2.append(' ')
            k3.append('*')
        elif a == 'R':
            k1.append(d1[i])
            i += 1
            k2.append(d2[j])
            j += 1
            k3.append('-')
        else:
            k1.append(d1[i])
            i += 1
            k2.append(d2[j])
            j += 1
            k3.append('+')

    return [''.join(s) for s in [k1, k2, k3]]

def test(dna1, dna2, copy, replace, insert, delete):
    plan = align_plan(dna1, dna2, copy, replace, insert, delete)
    for p in plan:
        print(p)

def main():
    '''利用最短编辑距离算法处理DNA对齐问题'''
    test('GATCGGCAT', 'CAATGTGAATC', -1, 1, 2, 2)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
