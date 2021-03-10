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
    def mirror(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.mirror(root.left)
        self.mirror(root.right)
        root.left, root.right = root.right, root.left
        return root

def validate(e, r) -> bool:
    # logger.info('in validate')
    if not e and not r:
        return True
    elif e and r:
        return e.val == r.val and validate(e.left, r.left) and validate(e.right, r.right)
    return False

if __name__ == '__main__':
    init_logging()
    from soda.unittest.work import TestWork

    # step [2]: setup function
    # Attention! FUNCTION must use type hint, including arguments and return type
    work = TestWork(Solution().mirror)

    # step [3]: setup other options
    work.validator = validate
    # work.compareSerial = True
    # work.setArgumentParser(index, (a) => b)
    # work.resultSerializer = (r) => s
    # work.resultParser = (s) => r
    work.run()

