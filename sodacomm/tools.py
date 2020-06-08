import functools
import sys
import time

__test_number = 0

def execute(func, args, kwargs, *, show_args=True, show_result=True, validator=None):
    # show test number
    global __test_number
    __test_number += 1
    print(f'**[{__test_number}]**')

    # show args and kwargs
    def print_args(*_args, **_kwargs):
        print('args:', _args, 'kwargs:', _kwargs)
    if show_args is True:
        show_args = print_args
    if callable(show_args):
        print('input:')
        show_args(*args, **kwargs)

    # record start time
    t1 = time.time()

    # execute testing procedure
    res = func(*args, **kwargs)

    # record end time
    t2 = time.time()

    # validate result object
    if validator is not None:
        if callable(validator):
            if not validator(res):
                raise Exception(f'Wrong answer {res}, failed to the validator')
        elif res != validator:
            raise Exception(f'Wrong answer {res}, but {validator} expected')

    # show result
    def print_result(_res):
        print(res)
    if show_result is True:
        show_result = print_result
    if callable(show_result):
        print('output:')
        show_result(res)

    # show end flag
    print(f'----')

    # show time elapsed
    print(f'{(t2-t1)*1000:.3f} ms\n')

    return res

def simpletest(func):
    @functools.wraps(func)
    def _test(*args, **kwargs):
        return execute(func, args, kwargs, show_args=False, show_result=False)
    return _test

testwrapper = simpletest

def sodatest(repeat=1,show_args=True,show_result=True,validator=None):
    def _wrapper(func):
        @functools.wraps(func)
        def runner(*args, **kwargs):
            for i in range(max(1,repeat)):
                res = execute(
                        func, args, kwargs,
                        show_args = show_args,
                        show_result = show_result,
                        validator = validator
                      )
            return res
        return runner
    return _wrapper

def testrun(func, *args, **kwargs):
    execute(func, args, kwargs)

def testcall(func, args=(), kwargs={}, *, show_args=True, show_result=True, validator=None, answer=None):
    if not isinstance(args, (tuple)):
        args = (args,)
    if validator is None and answer is not None:
        validator = answer
    execute(
        func, args, kwargs,
        show_args = show_args,
        show_result = show_result,
        validator = validator
    )

def justtest(args, answer):
    func = sys.modules['__main__'].solution
    testcall(func, args, answer=answer)

class Validator:

    @classmethod
    def seq(cls, seq):
        def validate(res):
            s = list(seq)
            i = 0
            n = len(s)
            for r in res:
                if i == n or s[i] != r:
                    return False
                i += 1
            return i == n
        return validate

    @classmethod
    def set(cls, seq):
        def validate(res):
            s = set(seq)
            n = len(s)
            count = 0
            for r in res:
                if r not in s:
                    return False
                s.remove(r)
                count += 1
            return count == n
        return validate

class ObjectDumper:

    @classmethod
    def matrix(cls, mx):
        print('[')
        for row in mx:
            print(' ', row)
        print(']')

