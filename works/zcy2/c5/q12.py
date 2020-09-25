#!/usr/bin/env python3
import sys

from sodacomm.tools import testwrapper

def min_dist(strs, s1, s2):
    last_1 = last_2 = -1
    md = sys.maxsize
    for i, s in enumerate(strs):
        if s == s1:
            if last_2 >= 0:
                md = min(md, i - last_2)
            last_1 = i
        elif s == s2:
            if last_1 >= 0:
                md = min(md, i - last_1)
            last_2 = i
    return md if md < sys.maxsize else -1

def min_dist_2(strs, s1, s2):
    rec = make_record(strs)
    return rec.get(s1, {}).get(s2, -1)

def make_record(strs):
    rec = {}
    idx = {}
    for i, s in enumerate(strs):
        do_update(rec, idx, s, i)
        idx[s] = i
    return rec

def do_update(rec, idx, s, i):
    if s not in rec:
        rec[s] = {}
    for _str, _loc in idx.items():
        if _str == s:
            continue
        cur_dist = i - _loc
        old_dist = rec[_str].get(s, sys.maxsize)
        rec[_str][s] = rec[s][_str] = min(cur_dist, old_dist)

@testwrapper
def test(strs, s1, s2):
    print(strs, s1, s2)
    print(min_dist(strs, s1, s2))
    print(min_dist_2(strs, s1, s2))

def main():
    test(['1','3','3','3','2','3','1'], '1', '2')
    test(['cd'], 'cd', 'ab')

if __name__ == '__main__':
    main()
