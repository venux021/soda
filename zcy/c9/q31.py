#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def pattern(t):
    n = len(t)
    if n == 1:
        return [-1]
    elif n == 2:
        return [-1, 0]
    p = [0] * n
    p[0] = -1

    j = 0
    i = 1

    while i < n - 1:
        if j == -1 or t[i] == t[j]:
            j += 1
            i += 1
            if t[i] != t[j]:
                p[i] = j
            else:
                p[i] = p[j]
        else:
            j = p[j]

    return p

def find(s, t):
    n = len(s)
    m = len(t)
    p = pattern(t)

    i = j = 0
    while i < n and j < m:
        if s[i] == t[j] or j == -1:
            i += 1
            j += 1
        else:
            j = p[j]
    return i - m if j == m else -1

def test(s, t):
    print 's: {}, t: {}'.format(s, t)
    print 'index: {}'.format(find(s, t))

def main():
    '''KMP算法'''
    test('acbc', 'bc')
    test('acbc', 'bcc')
    test('acbcdeckdwereuo', 'eckdwer')
    test('acbcdeckdwereuo', 'acbcdec')
    test('acbcdeckdwereuo', 'dwereuo')
    test('aaabaaaacaaaaabaa', 'aaaaab')
    test('aaabaabcdabckaacaaaaabaa', 'abcdabck')
    test('aaabaabcdabckaacaaaaabaa', 'abc1abc1')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
