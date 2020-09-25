#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def replace_blank(s):
    buf = list(s) * 2
    n = len(s)

    c = 0
    for i in range(n):
        if s[i] == ' ':
            c += 1

    if c == 0:
        return s

    new_len = n + c*2

    j = new_len - 1
    i = n - 1
    while i >= 0:
        if buf[i] != ' ':
            buf[j] = buf[i]
            j -= 1
            i -= 1
        else:
            buf[j] = '0'
            buf[j-1] = '2'
            buf[j-2] = '%'
            j -= 3
            i -= 1

    return ''.join(buf[:new_len])

def test(s):
    print('origin:', s)
    print('new:', replace_blank(s))

def main():
    '''替换空格'''
    test('We are happy.')
    test('One blank.')
    test('Noblank.')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
