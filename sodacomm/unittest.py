import sys

from sodacomm.tools import *

class Tester:

    def __init__(self):
        self.show_args = True
        self.show_result = True
        self.validator = None

    def call(self, func, args=(), kwargs={}, answer=None):
        validator = answer or self.validator
        testcall(
            func, args, kwargs,
            show_args=self.show_args,
            show_result=self.show_result,
            validator=validator
        )

    def just(self, args, answer):
        func = sys.modules['__main__'].solution
        self.call(func, args, answer=answer)

    def all(self, types, source = 'input_data.txt'):
        for case, res in load_case(types, source):
            self.just(case, res)
