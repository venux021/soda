#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def stripk(s,k):
    n = 0
    buf = []
    for c in s:
        if c == '0':
            n += 1
        else:
            if n > 0 and n != k:
                buf.append('0' * n)
            n = 0
            buf.append(c)
    if n > 0 and n != k:
        buf.append('0' * n)
    return ''.join(buf)

def test(s, k):
    print 's: {}, k: {}'.format(s,k)
    print 'r: {}'.format(stripk(s,k))

def main():
    '''去掉字符串中连续出现k个0的字串'''
    test('A000B', 3)
    test('A0000B000', 3)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
