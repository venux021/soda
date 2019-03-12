#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def build_post_seq(spre, sin):
    spost = [None] * len(spre)
    do_build(spre, sin, spost, len(spre)-1)
    return spost

def do_build(spre, sin, spost, iroot):
    if not spre:
        return
    root_v = spre[0]
    spost[iroot] = root_v
    i = sin.index(root_v)
    left_size = i
    right_size = len(spre) - 1 - i
    if left_size > 0:
        do_build(spre[1:1+left_size], sin[:i], spost, iroot - right_size - 1)
    if right_size > 0:
        do_build(spre[1+left_size:], sin[i+1:], spost, iroot - 1)

@testwrapper
def test(spre, sin):
    print(spre, sin)
    spost = build_post_seq(spre, sin)
    print(spost)

def main():
    test([1,2,4,5,3,6,7], [4,2,5,1,6,3,7])
    test([1,2,3,4,6,7,5], [1,4,7,6,3,5,2])

if __name__ == '__main__':
    main()
