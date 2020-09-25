#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def max_len(s):
    n = len(s)
    mx = [[0] * n for i in range(n)]

    for i in range(n):
        mx[i][i] = 1

    mxl = 1
    a = b = 0
    for L in range(2, n+1):
        for i in range(0, n-L+1):
            j = i + L - 1
            if L == 2:
                if s[i] == s[j]:
                    mx[i][j] = 2
                    if mxl < 2:
                        mxl = 2
                        a,b = i,j
            else:
                if s[i] == s[j] and mx[i+1][j-1] > 0:
                    mx[i][j] = mx[i+1][j-1] + 2
                    if mx[i][j] > mxl:
                        mxl = mx[i][j]
                        a,b = i,j
    return s[a:b+1]

def manacher_palindrome(s):
    n = len(s)
    N = 2*n+1
    sx = ['#'] * (2*n+1)

    for i, c in enumerate(s):
        sx[i*2+1] = c

    mxrd = [0] * (2*n+1)
    index = 0
    pmax = 1

    mxrd[0] = 1

    for i in range(1, 2*n+1):
        if i >= pmax:
            j = i - 1
            while j >= 0 and i*2-j < N and sx[j] == sx[i*2-j]:
                j -= 1
            length = i - j
            right_most = i + length
            if right_most > pmax:
                index = i
                pmax = right_most
            mxrd[i] = length
        else:
            j = index * 2 - i
            span = mxrd[j]
            left_most = index - mxrd[index] + 1
            j_left = j - span + 1
            if j_left > left_most:
                mxrd[i] = span
            elif j_left < left_most:
                mxrd[i] = j - left_most + 1
            else:
                k = i - j + left_most
                while k >= 0 and i*2-k < N and sx[k] == sx[i*2-k]:
                    k -= 1
                mxrd[i] = i - k

    max_i = 0
    for i in range(1, N):
        if mxrd[i] > mxrd[max_i]:
            max_i = i

    L = mxrd[max_i]
    return ''.join(sx[max_i-L+1:max_i+L][1:-1:2])

def append(s):
    n = len(s)
    N = 2*n+1
    sx = ['#'] * (2*n+1)

    for i, c in enumerate(s):
        sx[i*2+1] = c

    mxrd = [0] * (2*n+1)
    index = 0
    pmax = 1

    mxrd[0] = 1

    for i in range(1, 2*n+1):
        if i >= pmax:
            j = i - 1
            while j >= 0 and i*2-j < N and sx[j] == sx[i*2-j]:
                j -= 1
            length = i - j
            mxrd[i] = length
            right_most = i + length
            if right_most > pmax:
                index = i
                pmax = right_most
                if pmax == N:
                    break
        else:
            j = index * 2 - i
            span = mxrd[j]
            left_most = index - mxrd[index] + 1
            j_left = j - span + 1
            if j_left > left_most:
                mxrd[i] = span
            elif j_left < left_most:
                mxrd[i] = j - left_most + 1
            else:
                k = i - j + left_most
                while k >= 0 and i*2-k < N and sx[k] == sx[i*2-k]:
                    k -= 1
                mxrd[i] = i - k

    len_palind = mxrd[index] - 1

    return s + s[:n-len_palind][::-1]


def test(s):
    print 's: {}'.format(s)
    print 'max p : {}'.format(max_len(s))
    print 'mana p: {}'.format(manacher_palindrome(s))
    print 'append: {}'.format(append(s))
    print '----'

def main():
    '''Manacher算法'''
    test('123')
    test('1223')
    test('abc1234321ab')
    test('421abcba1234321ac')
    test('421abcba1234321ab')
    test('12345654321')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
