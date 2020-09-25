#!/usr/bin/env python3
import sys

def hanoi_s(n, x, y, z):
    ls = [sys.maxsize]
    ms = [sys.maxsize]
    rs = [sys.maxsize]
    NO, LM, ML, RM, MR = 0,1,2,3,4
    last = LM

    for i in range(n, 1, -1):
        ls.append(i)
    ms.append(1)
    
    print('1: {} -> {}'.format(x, y))
    steps = 1
    while len(rs) <= n:
        if last == LM or last == ML:
            if ms[-1] < rs[-1]:
                print('{}: {} -> {}'.format(ms[-1], y, z))
                rs.append(ms.pop())
                last = MR
            else:
                print('{}: {} -> {}'.format(rs[-1], z, y))
                ms.append(rs.pop())
                last = RM
        else:
            if ls[-1] < ms[-1]:
                print('{}: {} -> {}'.format(ls[-1], x, y))
                ms.append(ls.pop())
                last = LM
            else:
                print('{}: {} -> {}'.format(ms[-1], y, x))
                ls.append(ms.pop())
                last = ML
        steps += 1

    return steps

def hanoi_r(n, x, y, z):
    if n > 1:
        k = hanoi_r(n-1, x, y, z)
        print('{}: {} -> {}'.format(n, x, y))
        k += hanoi_r(n-1, z, y, x)
        print('{}: {} -> {}'.format(n, y, z))
        k += hanoi_r(n-1, x, y, z)
        return k + 2
    else:
        print('1: {} -> {}'.format(x, y))
        print('1: {} -> {}'.format(y, z))
        return 2

def test(n):
    k = hanoi_s(n, 'a', 'b', 'c')
    print('rank: {}, total steps: {}'.format(n, k))
    print('+++++++++')
    k = hanoi_r(n, 'a', 'b', 'c')
    print('rank: {}, total steps: {}'.format(n, k))
    print('---------')

def main():
#    test(2)
    test(3)
#    test(5)
#    test(10)

if __name__ == '__main__':
    main()
