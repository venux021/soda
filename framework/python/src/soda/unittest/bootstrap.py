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

if __name__ == '__main__':
    init_logging()
    from soda.unittest.job import JobEntry
    # class, method name, return type, arg types
    JobEntry.run(Solution, '', _, _)

#    JobEntry.run(
#        cls = Solution,               # solution class
#        method = '',                  # method name
#        ret_type = ...,               # return type
#        arg_types = ...,              # argument types
#        validate_by_object = False,   # true - validate between expected and result in original type
#                                      # false - in serialized type
#        object_validator = None,      # perform when validate_by_object is true
#        serial_validator = None       # perform when validate_by_object is false
#    )
