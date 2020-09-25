#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def get_post(pre, ins):
    n = len(pre)
    post = [' '] * n
    _post(n, pre, 0, ins, 0, post, 0)
    return ' '.join(post)

def _post(n, pre, pre_s, ins, ins_s, post, post_s):
    if n <= 0:
        return

    root = pre[pre_s]
    post[post_s + n - 1] = root

    i = ins_s
    j = ins_s + n
    while i < j and ins[i] != root:
        i += 1

    left_size = i - ins_s
    right_size = n - left_size - 1
    
    _post(left_size, pre, pre_s+1, ins, ins_s, post, post_s)
    _post(right_size, pre, pre_s+1+left_size, ins, i+1, post, post_s+left_size)

def test(pre, ins):
    pre = pre.split(' ')
    ins = ins.split(' ')
    print(pre, ins, get_post(pre, ins))

def main():
    '''通过先序和中序数组生成后序数组'''
    test('a b d e c f', 'd b e a c f')    
    test('a b d c f', 'd b a c f')    
    test('a b c d', 'd c b a')
    test('a b c d', 'a b c d')

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
