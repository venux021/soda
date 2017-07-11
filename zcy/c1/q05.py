#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def sort(stk):
    k = []

    while stk:
        i = stk.pop()
        while k and k[-1] > i:
            stk.append(k.pop())
        k.append(i)

    while k:
        stk.append(k.pop())


def test(stk):
    print(stk)
    sort(stk)
    print(stk)
    print('-----')

def main():
    '''用一个栈实现另一个栈的排序'''
    test([3,2,4,1,5])
    test([3,3,2,2,4,4,1,1,5,5])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
