#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def ugly_number(n):
    buf = [0] * n
    p2 = p3 = p5 = 0
    k2 = 2
    k3 = 3
    k5 = 5
    buf[0] = 1
    c = 1
    
    while c < n:
        if k2 <= k3 and k2 <= k5:
            if k2 > buf[c-1]:
                buf[c] = k2
                c += 1
            p2 += 1
            k2 = buf[p2] * 2
        elif k3 <= k2 and k3 <= k5:
            if k3 > buf[c-1]:
                buf[c] = k3
                c += 1
            p3 += 1
            k3 = buf[p3] * 3
        else:
            if k5 > buf[c-1]:
                buf[c] = k5
                c += 1
            p5 += 1
            k5 = buf[p5] * 5

    return buf[-1]

def test(n):
    print('No {} ugly number is {}'.format(n, ugly_number(n)))

def main():
    '''丑数'''
    for i in range(1, 30):
        test(i)
    test(1500)

if __name__ == '__main__':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    main()
