#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def count(s, d):
    n = len(s)
    T = [[0] * n for i in range(n)]
    F = [[0] * n for i in range(n)]

    for i in range(0, n, 2):
        T[i][i] = 1 if s[i] == '1' else 0
        F[i][i] = 1 - T[i][i]

    for L in range(3, n+1, 2):
        i = 0
        j = i + L - 1
        while j < n:
            tc = 0
            fc = 0
            for k in range(i, j-1, 2):
                if s[k+1] == '&':
                    tc += (T[i][k] * T[k+2][j])
                    fc += (F[i][k] * (F[k+2][j]+T[k+2][j]) + (T[i][k]+F[i][k]) * F[k+2][j])
                elif s[k+1] == '|':
                    tc += (T[i][k] * (F[k+2][j]+T[k+2][j]) + (T[i][k]+F[i][k]) * T[k+2][j])
                    fc += (F[i][k] * F[k+2][j])
                else:
                    tc += ((T[i][k] * F[k+2][j]) + (F[i][k] * T[k+2][j]))
                    fc += ((T[i][k] * T[k+2][j]) + (F[i][k] * F[k+2][j]))
            T[i][j] = tc
            F[i][j] = fc
            i += 2
            j += 2

    return T[0][n-1] if d else F[0][n-1]

def test(s, d):
    print 's: {}, d: {}'.format(s, d)
    print 'result: {}'.format(count(s, d))

def main():
    '''表达式得到期望结果的组成种数'''
    test('1^0|0|1', False)
    test('1^0|0|1', True)
    test('1^0|0&1', False)
    test('1^0|0&1', True)
    test('1', False)
    test('1', True)
    test('1^0', True)
    test('1^0', False)
    test('1|0^0^1&0^1|0&0&1|0^1|0&1', True)
    test('1|0^0^1&0^1|0&0&1|0^1|0&1', False)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
