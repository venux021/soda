#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def longest_unique_sub(s):
    n = len(s)
    _set = set([s[0]])
    i = 0
    j = 1
    max_len = 1
    sub_start = 0
    while j < n:
        if s[j] not in _set:
            cur_len = j - i + 1
            _set.add(s[j])
            if cur_len > max_len:
                sub_start = i
                max_len = cur_len
            j += 1
        else:
            _set.remove(s[i])
            i += 1
    return s[sub_start:sub_start+max_len]

@testwrapper
def test(s):
    print(s)
    print(longest_unique_sub(s))

def main():
    test('abcd')
    test('aabcb')
    test('abcccde')

if __name__ == '__main__':
    main()
