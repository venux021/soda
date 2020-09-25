#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def get_jump_1(s):
    n = len(s)
    jump = [-1] * n
    for i in range(1,n):
        j = jump[i-1]
        while j != -1 and s[i-1] != s[j]:
            j = jump[j]
        jump[i] = j + 1
    return jump

def get_jump_2(s):
    n = len(s)
    jump = [0] * n
    jump[0] = -1
    j = -1
    i = 0
    while i < n-1:
        if j == -1 or s[i] == s[j]:
            i += 1
            j += 1
            if s[i] == s[j]:
                jump[i] = jump[j]
            else:
                jump[i] = j
        else:
            j = jump[j]
    return jump

def str_find(s, p):
    jump = get_jump_1(p)
#    jump = get_jump_2(p)
    i = j = 0
    while i < len(s) and j < len(p):
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = jump[j]
    return i - len(p) if j == len(p) else -1

@testwrapper
def test(s, p):
    print(s, p)
    print(get_jump_1(s))
    print(get_jump_2(s))
    print(str_find(s, p))

def main():
    test('aaaaaaaaaabaabaaaaaab', 'aaab')
    test('abcdefgabcdabc', 'defga')
    test('aaaabcd', 'aab')

if __name__ == '__main__':
    main()
