#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class Seg(object):

    def __init__(self, i):
        self.left = i
        self.right = i

    def merge(self, s):
        if self == s:
            return
        s.left = self.left = min(self.left, s.left)
        s.right = self.right = max(self.right, s.right)

    def size(self):
        return self.right - self.left + 1

def max_cont_seq(arr):
    n = len(arr)
    m = {}

    for v in arr:
        if v in m:
            continue
        left = v-1
        right = v+1
        if left in m and right in m:
            m[left].merge(m[right])
        elif left in m:
            m[left].right += 1
            m[v] = m[left]
        elif right in m:
            m[right].left += 1
            m[v] = m[right]
        else:
            m[v] = Seg(v)

    L = 0
    for s in m.values():
        L = max(L, s.size())

    return L
            

def test(arr):
    print 'arr: {}'.format(arr)
    print 'max conti seq: {}'.format(max_cont_seq(arr))

def main():
    '''数组中的最长连续序列'''
    test([100,4,200,1,3,2])

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
