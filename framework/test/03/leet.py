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
class Input1:
    def __init__(self, value):
        self.value = value

class Input2:
    def __init__(self, text):
        self.text = text

class Output:
    def __init__(self, value, text):
        self.val = value
        self.str = text

class Solution:
    def gen(self, i1: Input1, i2: Input2) -> Output:
        return Output(i1.value, i2.text)

if __name__ == '__main__':
    init_logging()
    from soda.unittest.work import TestWork

    # step [2]: setup function
    # Attention! FUNCTION must use type hint, including arguments and return type
    work = TestWork(Solution().gen)

    # step [3]: setup other options
    work.validator = lambda x, y: x.val == y.val and x.str == y.str
    # work.compareSerial = True
    # work.setArgumentParser(index, (a) => b)
    work.setArgumentParser(0, lambda x: Input1(x))
    work.setArgumentParser(1, lambda x: Input2(x))
    work.resultParser = lambda x: Output(len(x), x[0])
    work.resultSerializer = lambda x: [x.str] * x.val
    # work.resultSerializer = (r) => s
    # work.resultParser = (s) => r
    work.run()

