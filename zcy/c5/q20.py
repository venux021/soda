#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def sub_len(s1, s2):
    M = {}
    for c in s2:
        M[c] = M.get(c, 0) + 1

    match = len(s2)

    left = right = 0
    L = 0x7fffffff
    while right < len(s1):
        c = s1[right]
        if c not in M:
            right += 1
            continue
        M[c] = M.get(c, 0) - 1
        if M[c] == 0:
            match -= 1
            if match == 0:
                while True:
                    c = s1[left]
                    if c not in M:
                        left += 1
                        continue
                    if M[c] == 0:
                        break
                    else:
                        M[c] += 1
                        left += 1
                L = min(L, right - left + 1)
                M[s1[left]] += 1
                match += 1
        right += 1

    return L if L < 0x7fffffff else 0

def test(s1, s2):
    print 's1: {}, s2: {}'.format(s1, s2)
    print 'len: {}'.format(sub_len(s1, s2))

def main():
    '''最小包含子串的长度'''
    test('abcde', 'ac')
    test('12345', '344')
    test('adabbca', 'acb')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
