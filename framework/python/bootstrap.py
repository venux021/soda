#!/usr/bin/env python3
from collections import Counter, defaultdict, deque
import heapq
import json
import math
import random
import time
from typing import *
import sys

from soda.leetcode.bitree import *
from soda.leetcode.graph import *
from soda.leetcode.linklist import *

def solution():
    pass

def validate(res, answer):
    return res == answer

if __name__ == '__main__':
    buf = []
    for line in sys.stdin:
        buf.append(line)

    testobj = json.loads(''.join(buf))
    answer = testobj['answer']

    # get args from testobj['args']
    # TODO

    # start time
    start = time.time()

    # run test
    # TODO res = solution()

    # end time
    end = time.time()

    response = {
        'id': testobj['id'],
        'success': answer is None or validate(res, answer),
        'result': res,
        'elapse': (end-start) * 1000
    }
    print(json.dumps(response))
