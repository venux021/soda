#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def hanoi_2(n, a, b, c):
    L = [i for i in range(n, 0, -1)]
    M = []
    R = []
    L2M = 1
    M2L = 2
    M2R = 3
    R2M = 4
    step = 0
    last_act = None

    if n < 1:
        return

    print(f'Move 1 from left to mid')
    M.append(L.pop())
    last_act = L2M
    step += 1

    while len(R) < n:
        if last_act == L2M or last_act == M2L:
            if can_move(M, R):
                print(f'Move {M[-1]} from mid to right')
                R.append(M.pop())
                last_act = M2R
            else:
                print(f'Move {R[-1]} from right to mid')
                M.append(R.pop())
                last_act = R2M
        else:
            if can_move(L, M):
                print(f'Move {L[-1]} from left to mid')
                M.append(L.pop())
                last_act = L2M
            else:
                print(f'Move {M[-1]} from mid to left')
                L.append(M.pop())
                last_act = M2L
        step += 1
    return step

def can_move(a, b):
    return a and (not b or a[-1] < b[-1])

def hanoi_x(n, a, b, c):
    if n < 1:
        return 0
    else:
        t = 0
        t += hanoi_x(n-1, a, b, c)
        print(f'Move {n} from {a} to {b}')
        t += hanoi_x(n-1, c, b, a)
        print(f'Move {n} from {b} to {c}')
        t += hanoi_x(n-1, a, b, c)
        return t + 2

@testwrapper
def test(n):
    t = hanoi_2(n, 'left', 'mid', 'right')
    print(f'It will move {t} steps.')

def main():
    test(1)
    test(2)
    test(3)
    test(4)
    test(5)

if __name__ == '__main__':
    main()
