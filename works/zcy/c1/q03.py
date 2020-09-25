#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def reverse(stk):
    if not stk:
        return
    bottom = remove_bottom(stk)
    reverse(stk)
    stk.append(bottom)

def remove_bottom(stk):
    top = stk.pop()
    if not stk:
        return top
    bottom = remove_bottom(stk)
    stk.append(top)
    return bottom

def test(stk):
    print(stk)
    reverse(stk)
    print(stk)
    print('----')

def main():
    '''如何仅用递归函数和栈操作逆序一个栈'''
    test([1,2,3,4,5])
    test([1,2])
    test([1])

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
