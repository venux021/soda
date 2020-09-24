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
from soda.unittest.common import *

# step [0]: implement class Solution
# class Solution: pass

# step [1]: implement validate function
def validate(res, answer):
    return res == answer

if __name__ == '__main__':
    req = UnitTestRequest(json.load(sys.stdin))

    # step [2]: deserialize arguments
    # arg0 = req.arg(0)

    start = time.time()

    su = Solution()
    # step [3]: invoke solution function
    # res = su.someMethod(arg0, arg1, ...)

    end = time.time()

    resp = {
        'id': req.id,
        'elapse': (end-start) * 1000
    }

    if req.answer:
        # step [4]
        # 4.1 deserialize answer object
        # resp['success'] = validate(res, DESERIALIZE(req.answer))
        # 
        # OR
        # 
        # 4.2 compare serialized result with raw answer
        # resp['success'] = validate(SERIALIZE(res), req.answer)
    else:
        resp['success'] = True

    # step [5]: serialize result object if necessary
    # resp['result'] = SERIALIZE(res)

    print(json.dumps(resp))

