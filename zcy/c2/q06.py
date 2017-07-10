#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def get_surv(n, k):
    p = 0
    for i in range(2, n+1):
        p = (p+k) % i
    return p + 1

def test(n, k):
    print('n: {}, k:{}, survivor: {}'.format(n, k, get_surv(n,k)))

def main():
    '''环形单链表的约瑟夫问题'''
    test(1, 5)
    test(2, 5)
    test(5, 5)
    test(10, 5)
    test(10, 6)
    test(10, 7)
    test(10, 16)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
