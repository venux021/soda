#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def to_stat(s):
    buf = []
    cur_char = s[0]
    cur_num = 0
    for c in s:
        if c == cur_char:
            cur_num += 1
        else:
            buf.append(f'{cur_char}_{cur_num}')
            cur_char = c
            cur_num = 1
    buf.append(f'{cur_char}_{cur_num}')
    return '_'.join(buf)

def get_char(s, index):
    n = len(s)
    total = 0
    i = 0
    while i < n:
        ch = s[i]
        a = do_find(s, i)
        b = do_find(s, a + 1)
        num_s = s[a+1:b]
        k = to_num(num_s)
        total += k
        if total > index:
            return ch
        i = b + 1

def do_find(s, i):
    n = len(s)
    while i < n and s[i] != '_':
        i += 1
    return i

def to_num(s):
    k = 0
    for c in s:
        k = k * 10 + (ord(c) - ord('0'))
    return k

@testwrapper
def test(s, index):
    print(f'origin: {s}')
    stat_str = to_stat(s)
    print(f'stat: {stat_str}')
    ch = get_char(stat_str, index)
    print(f'char[{index}]: {ch}')

def main():
    test('aaabbadddffc', 7)
    test('aaabbadddffc', 0)
    test('aaabbadddffc', 20)
    test('abbbbbbbbbbbbbbbb', 0)
    test('abbbbbbbbbbbbbbbb', 14)

if __name__ == '__main__':
    main()
