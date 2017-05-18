#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def replace(s,f,t):
    r = []
    i = 0
    while True:
        j = s.find(f, i)
        if j < 0:
            break
        if i < j:
            r.append(s[i:j])
            r.append(t)
        i += len(f)

    r.append(s[i:])

    return ''.join(r)

def test(s, f, t):
    print 's: {}, f: {}, t: {}'.format(s,f,t)
    print 'replace: {}'.format(replace(s,f,t))

def main():
    '''替换字符串中连续出现的指定字符串'''
    test('123abc', 'abc', '4567')
    test('123', 'abc', '456')
    test('123abcabc', 'abc', 'X')

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
