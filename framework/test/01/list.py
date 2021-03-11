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
class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        h = None
        while head:
            n = head.next
            head.next = h
            h = head
            head = n
        return h

def validate(e, r) -> bool:
    while e and r:
        if e.val != r.val:
            return False
        e = e.next
        r = r.next
    return e == r

def parseResult(listData):
    # logging.info('in parseResult')
    return ListFactory.create(listData)

def serialResult(head):
    # logging.info('in serialResult')
    return ListFactory.dump(head)

def parseArg(listData):
    # logging.info('in parseArg')
    return ListFactory.create(listData)

if __name__ == '__main__':
    init_logging()
    from soda.unittest.work import TestWork

    # step [2]: setup function
    # Attention! FUNCTION must use type hint, including arguments and return type
    work = TestWork(Solution().reverse)

    # step [3]: setup other options
    work.validator = validate
    # work.compareSerial = True
    work.setArgumentParser(0, parseArg)
    work.resultSerializer = serialResult
    work.resultParser = parseResult
    work.run()

