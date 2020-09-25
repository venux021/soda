#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

class Section(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def merge(self, other):
        self.start = min(self.start, other.start)
        self.end = max(self.end, other.end)

def by_order(s):
    r = []
    mstart = {}
    mend = {}
    next_i = 1
    for i in s:
        if i > next_i:
            sec = Section(i, i)
            if i+1 in mstart:
                sec.merge(mstart[i+1])
                del mstart[i+1]
                mend[sec.end] = sec
            else:
                mend[i] = sec
            if i-1 in mend:
                sec.merge(mend[i-1])
                del mend[i-1]
                mstart[sec.start] = sec
            else:
                mstart[i] = sec
        elif i == next_i:
            r.append(i)
            next_i += 1
            if i+1 in mstart:
                for j in range(mstart[i+1].start, mstart[i+1].end+1):
                    r.append(j)
                    next_i += 1
                a = mstart[i+1].start
                b = mstart[i+1].end
                del mstart[a]
                del mend[b]
    return r

def test(n):
    s = gen_seq(n)
    print 'seq: {}'.format(s)
    print 'r: {}'.format(by_order(s))

def gen_seq(n):
    s = [i+1 for i in range(n)]
    random.shuffle(s)
    return s

def main():
    '''一种消息接收并打印的结构设计'''
    test(30)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
