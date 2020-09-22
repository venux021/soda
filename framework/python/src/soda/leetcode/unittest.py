import sys

from sodacomm.tools import *

class Tester:

    def __init__(self):
        self.show_args = True
        self.show_result = True
        self.validator = lambda res, ans: res == ans

    def call(self, func, args=(), kwargs={}, answer=None, skip=False):
        if not isinstance(args, (tuple)):
            args = (args,)
        execute(
            func, args, kwargs,
            show_args=self.show_args,
            show_result=self.show_result,
            answer=answer,
            checker=self.validator,
            skip=skip
        )

    def just(self, args, answer, skip=False):
        func = sys.modules['__main__'].solution
        self.call(func, args, answer=answer, skip=skip)

    def all(self, types, source = 'input_data.txt', active=None):
        if isinstance(source, str):
            source = [source]
        seq = 0
        if active is not None:
            active = set(active)
        for datafile in source:
            for case, res in load_case(types, datafile):
                seq += 1
                if not active or seq in active:
                    self.just(case, res)
                else:
                    self.just(case, res, skip=True)

    def load_case(self, types, target_seq, source = 'input_data.txt'):
        if isinstance(source, str):
            source = [source]
        seq = 0
        for datafile in source:
            for case, res in load_case(types, datafile):
                seq += 1
                if seq == target_seq:
                    return (case, res)

    def do(self, *args, ans):
        self.just(args, ans)

