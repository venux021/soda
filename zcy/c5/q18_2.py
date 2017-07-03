#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def max_uniq_len(s):
    n = len(s)
    loc = {}
    pre = -1
    d = -1
    L = 0

    for i in range(n):
        if s[i] in loc:
            d = loc[s[i]]
        else:
            d = -1
        k = max(d, pre)
        L = max(L, i - k)
        pre = k
        loc[s[i]] = i

    return L


def test(s):
    print 's: {}'.format(s)
    print 'max uniq len: {}'.format(max_uniq_len(s))

def main():
    '''找到字符串的最长无重复字符子串'''
    test('abcd')
    test('aabcb')
    test('axubcbb')
    test('aabbccd')
    test('aabbcc')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
