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
    testobj = json.load(sys.stdin)
    req = UnitTestRequest(testobj)

    # step [2]: deserialize arguments
    # arg0 = req.arg(0)

    start = time.time()

    su = Solution()
    # step [3]: invoke solution function
    # res = su.someMethod(arg0, arg1, ...)

    end = time.time()

    response = {
        'id': testobj['id'],
        'elapse': (end-start) * 1000
    }

    if req.answer:
        # step [4]: deserialize answer object
        # answer = _deserialize(req.answer);
        response['success'] = validate(res, answer)
    else:
        response['success'] = True

    # step [5]: serialize result object
    # serialRes = _serialize(res);
    response['result'] = serialRes

    print(json.dumps(response))

