#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def min_sub(s1, s2):
    cstat = make_stat(s2)
    cs = {k:0 for k in cstat}
    n1 = len(s1)
    n2 = len(s2)
    k = 0
    i = j = 0
    min_len = sys.maxsize
    while j < n1 or k == n2:
        if k < n2:
            if s1[j] in cs and cs[s1[j]] < cstat[s1[j]]:
                cs[s1[j]] += 1
                k += 1
            j += 1
        else:
            min_len = min(min_len, j - i)
            if s1[i] in cs and cs[s1[i]] > 0:
                cs[s1[i]] -= 1
                k -= 1
            i += 1
    return min_len if min_len < sys.maxsize else 0

def make_stat(s):
    cs = {}
    for c in s:
        cs[c] = cs.get(c, 0) + 1
    return cs

@testwrapper
def test(s1, s2):
    print(s1, s2)
    print(min_sub(s1, s2))

def main():
    test('deabc', 'ac')
    test('abcde', 'ac')
    test('12345', '344')
    test('467cxycjbkbbatyd123', 'abccd')

if __name__ == '__main__':
    main()
