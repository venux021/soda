#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def long2(s):
    m = [-1] * 256
    a = b = -1
    j = -1
    max_len = 0

    for i in range(len(s)):
        j = max(j, m[ord(s[i])])
        L = i - j
        if L > max_len:
            a = j
            b = i
            max_len = L
        m[ord(s[i])] = i

    return s[a+1:b+1]

def longest_uniq_str(s):
    m = [0] * 256
    a = b = i = j = 0
    L = max_len = 0
    for i in range(len(s)):
        k = ord(s[i])
        if m[k] == 0:
            m[k] = 1
            L = i - j + 1
            if L > max_len:
                a = i
                b = j
                max_len = L
        else:
            while s[j] != s[i]:
                k = ord(s[j])
                m[k] = 0
                j += 1
            j += 1
    return s[b:a+1]

def test(s):
    print 's: {}, k1: {}, k2: {}'.format(s, longest_uniq_str(s), long2(s))

def main():
    '''找到字符串的最长无重复字串'''
    test('abcd')
    test('aabcb')
    test('aaaa')
    test('aabbcc')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
