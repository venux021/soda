#!/usr/bin/env python3
from collections import Counter, defaultdict, deque
import heapq
import json
import logging
import math
import random
import time
from typing import *
import sys

from soda.leetcode.bitree import *
from soda.leetcode.graph import *
from soda.leetcode.linklist import *
from soda.unittest.util import init_logging

logger = logging.getLogger(__name__)

# step [1]: implement class Solution
# class Solution: pass
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.N = len(times)
        self.times = times
        self.winner = [-1] * self.N
        self.initialize(persons)

    def initialize(self, persons):
        counter = {}
        counter[-1] = 0
        win = -1
        vote = 0
        for i in range(self.N):
            v = counter.get(persons[i], 0) + 1
            if v >= vote:
                win = persons[i]
                vote = v
            counter[persons[i]] = v
            self.winner[i] = win

    def q(self, t: int) -> int:
        if t >= self.times[-1]:
            return self.winner[-1]
        low, high = 0, self.N-1
        while low < high:
            mid = (low + high) // 2
            if t <= self.times[mid]:
                high = mid
            else:
                low = mid + 1
        return self.winner[low] if t == self.times[low] else self.winner[low-1]

class Params:
    def __init__(self):
        self.persons = None
        self.times = None
        self.qs = None

class Solution:
    def doTest(self, commands: List[str], params: Params) -> List[int]:
        res = []
        tvc = None
        for i, cmd in enumerate(commands):
            if cmd == 'TopVotedCandidate':
                tvc = TopVotedCandidate(params.persons, params.times)
                res.append(None)
            else:
                res.append(tvc.q(params.qs[i]))
        return res

def params_parser(p):
    params = Params()
    params.persons = p[0][0]
    params.times = p[0][1]
    params.qs = [-1] * len(p)
    for i in range(1, len(p)):
        params.qs[i] = p[i][0]
    return params

if __name__ == '__main__':
    init_logging()
    from soda.unittest.work import TestWork

    # step [2]: setup function
    # Attention! FUNCTION must use type hint, including arguments and return type
    work = TestWork(Solution().doTest)

    # step [3]: setup other options
    # work.validator = (e,r) => bool
    work.compareSerial = True
    work.setArgumentParser(1, params_parser)
    # work.setArgumentParser(index, (a) => b)
    # work.resultSerializer = (r) => s
    # work.resultParser = (s) => r
    work.run()

