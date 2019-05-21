#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def rep_select(seq, M):
    tree = [M] * M
    buf = [(-1,0)] * (M+1)
    sections = []

    it = iter(seq)
    for i in range(M):
        num = next(it)
        buf[i] = (0,num)
        adjust(tree, M, buf, i)

    block_id = -1
    sec = []
    while True:
        win = tree[0]
        if buf[win][1] == sys.maxsize:
            break
        if buf[win][0] > block_id:
            block_id += 1
            if sec:
                sections.append(sec)
                sec = []
        minimax = buf[win][1]
        sec.append(minimax)
        try:
            num = next(it)
        except StopIteration:
            num = sys.maxsize
        if num >= minimax:
            buf[win] = (block_id, num)
        else:
            buf[win] = (block_id+1, num)
        adjust(tree, M, buf, win)
    if sec:
        sections.append(sec)

    return sections

def adjust(tree, k, buf, i):
    t = (i+k) // 2
    while t > 0:
        if buf[i] > buf[tree[t]]:
            tree[t], i = i, tree[t]
        t //= 2
    tree[0] = i

@testwrapper
def test(arr, M):
    print(arr)
    print(rep_select(arr, M))

def main():
    test([51,49,39,46,38,29,14,61,15,30,1,48,52,3,63,27,4,13,89,24,46,58,33,76], 6)

if __name__ == '__main__':
    main()
