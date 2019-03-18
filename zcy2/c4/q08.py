#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def longest_common_sub(s1, s2):
    m = len(s1)
    n = len(s2)
    max_size = 0
    max_i, max_j = -1, -1
    dp = 0
    for k in range(m):
        if s1[k] == s2[0]:
            dp = 1
        else:
            dp = 0
        if dp > max_size:
            max_size = dp
            max_i = k
            max_j = 0
        i = k + 1
        j = 1
        while i < m and j < n:
            if s1[i] == s2[j]:
                dp += 1
            else:
                dp = 0
            if dp > max_size:
                max_size = dp
                max_i = i
                max_j = j
            i += 1
            j += 1

    for k in range(1, n):
        if s2[k] == s1[0]:
            dp = 1
        else:
            dp = 0
        if dp > max_size:
            max_size = dp
            max_i = 0
            max_j = k
        i = 1
        j = k + 1
        while i < m and j < n:
            if s1[i] == s2[j]:
                dp += 1
            else:
                dp = 0
            if dp > max_size:
                max_size = dp
                max_i = i
                max_j = j
            i += 1
            j += 1

    if max_size == 0:
        return ''
    else:
        return s1[max_i-max_size+1:max_i+1]

@testwrapper
def test(s1, s2):
    print(s1, s2)
    print(longest_common_sub(s1, s2))

def main():
    test('1AB2345CD', '12345EF')
    test('abcde', '12345')

if __name__ == '__main__':
    main()
