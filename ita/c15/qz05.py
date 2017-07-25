#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

MAX = sys.maxsize

def minimum_edit_cost(src, dest, copy, replace, delete, insert, twiddle, kill):
    m = len(src)
    n = len(dest)
    dp = [[0] * (n+1) for i in range(m+1)]
    src = [''] + list(src)
    dest = [''] + list(dest)
    op = [[0] * (n+1) for i in range(m+1)]

    for i in range(1, m+1):
        dp[i][0] = delete * i
        op[i][0] = 'delete'
    for j in range(1, n+1):
        dp[0][j] = insert * j
        op[0][j] = 'insert'

    for i in range(1, m+1):
        for j in range(1, n+1):
            if src[i] == dest[j]:
                c_copy = dp[i-1][j-1] + copy
            else:
                c_copy = MAX
            c_replace = dp[i-1][j-1] + replace
            c_del_ins = dp[i-1][j-1] + delete + insert
            c_delete = dp[i-1][j] + delete
            c_insert = dp[i][j-1] + insert
            if i >= 2 and j >= 2 and src[i] == dest[j-1] and src[i-1] == dest[j]:
                c_twiddle = dp[i-2][j-2] + twiddle
            else:
                c_twiddle = MAX

            dp[i][j] = min(c_copy, c_replace, c_del_ins, c_delete, c_insert, c_twiddle)
            if dp[i][j] == c_copy:
                op[i][j] = 'copy'
            elif dp[i][j] == c_replace:
                op[i][j] = 'replace'
            elif dp[i][j] == c_del_ins:
                op[i][j] = 'del+ins'
            elif dp[i][j] == c_delete:
                op[i][j] = 'delete'
            elif dp[i][j] == c_insert:
                op[i][j] = 'insert'
            elif dp[i][j] == c_twiddle:
                op[i][j] = 'twiddle'

    i = m
    j = n
    min_cost = dp[m][n]
    for k in range(1, m):
        if dp[k][n] + kill < min_cost:
            i = k
            min_cost = dp[k][n] + kill

    op_list = []
    if i < m:
        op_list.append('kill')

    while i > 0 and j > 0:
        t = op[i][j]
        op_list.append(op[i][j])
        if t == 'copy' or t == 'replace' or t == 'del+ins':
            i -= 1
            j -= 1
        elif t == 'delete':
            i -= 1
        elif t == 'insert':
            j -= 1
        else:
            i -= 2
            j -= 2

    print(op_list[::-1])

    return min_cost

def test(src, dest, costs):
    print('{} -> {}, {}'.format(src, dest, minimum_edit_cost(
                    src, dest, costs['copy'], costs['replace'],
                    costs['delete'], costs['insert'], costs['twiddle'],
                    costs['kill'])))

def main():
    '''最短编辑距离'''
    test('algorithm', 'altruistic', 
            {
                'copy': 3,
                'replace': 4,
                'delete': 2,
                'insert': 5,
                'twiddle': 2,
                'kill': 5
            })

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
