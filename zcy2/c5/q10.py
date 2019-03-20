#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def inplace_blank(arr):
    c = 0
    for i, ch in enumerate(arr):
        if ch == ' ':
            c += 1
        elif ch is None:
            break
    old_len = i
    new_len = old_len + c * 2
    p = new_len - 1
    j = old_len - 1
    while p != j:
        if arr[j] != ' ':
            arr[p] = arr[j]
            p -= 1
        else:
            arr[p] = '0'
            arr[p-1] = '2'
            arr[p-2] = '%'
            p -= 3
        j -= 1

@testwrapper
def test(s):
    n = len(s)
    buf = [None] * n * 3
    buf[0:n] = list(s)
    inplace_blank(buf)
    print(s)
    print(''.join(filter(None, buf)))

def main():
    test('a b  c')
    test('  ab c ')
    test('     a')
    test('a     ')

if __name__ == '__main__':
    main()
