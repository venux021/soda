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
from soda.unittest.common import *

logger = logging.getLogger(__name__)

# step [1]: implement class Solution
# class Solution: pass

# step [2]: implement test job
class TestJob(JobTemplate):

    def execute(self, req: TestRequest, resp: TestResponse) -> 'ResultType':
        # TODO
        raise Exception('Not implemented')

    def serialize(self, res: 'ResultType') -> 'ResultSerialType':
        return res

    def validate(self, req: TestRequest, resp: TestResponse) -> bool:
        return req.expected == resp.result


if __name__ == '__main__':

    logging.basicConfig(
        level = logging.INFO,
        datefmt = '%Y-%m-%d %H:%M:%S',
        #format = '%(asctime)s [%(process)d] [%(name)s] %(levelname)s: %(message)s'
        format = '%(levelname)s: %(message)s'
    )

    req = TestRequest(json.load(sys.stdin))
    resp = TestResponse()
    resp.obj['id'] = req.id

    job = TestJob()

    start = time.time()
    res = job.run(req, resp)
    end = time.time()

    resp.obj['elapse'] = (end-start) * 1000

    if req.expected is not None:
        resp.obj['success'] = job.validate(req, resp)
    else:
        resp.obj['success'] = True

    print(json.dumps(resp.obj))

