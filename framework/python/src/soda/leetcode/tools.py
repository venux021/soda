import collections
import functools
import json
import sys
import time

__test_number = 0

class TestContext:

    def __init__(self):
        self.args = None
        self.kwargs = None

__test_context = TestContext()

def current_test_context():
    return __test_context

def execute(func, args, kwargs, *, 
        show_args=True, show_result=True, validator=None,
        answer=None, checker=None, skip=False):
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

    if skip:
        print('SKIP\n')
        return

    # record start time
    t1 = time.time()

    current_test_context().args = args
    current_test_context().kwargs = kwargs
    # execute testing procedure
    res = func(*args, **kwargs)

    # record end time
    t2 = time.time()

    # validate result object
    if checker is None:
        if callable(validator):
            checker = lambda res, _: validator(res)
        else:
            answer = validator
            checker = lambda res, _: res == validator
    if answer is not None and not checker(res, answer):
        info = f'Wrong answer {res}, but {answer} expected'
        raise Exception(info)

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

def load_case(types, source = 'input_data.txt'):
    def load_groups():
        with open(source, 'rt') as fp:
            group = []
            for line in fp:
                text = line.strip()
                if not text or text[0] == '#':
                    continue
                #if not group and not text:
                #    continue
                group.append(text)
                if len(group) > len(types):
                    yield group
                    group.clear()

    for group in load_groups():
        input_args = group[:-1]
        for i in range(len(types)):
            input_args[i] = json.loads(input_args[i])
        res = json.loads(group[-1])
        yield (tuple(input_args), res)

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
            errors = []
            for r in res:
                if r not in s:
                    errors.append(r)
                else:
                    s.remove(r)
            if s:
                print('Missing', s)
            if errors:
                print('Error result', errors)
            return not s and not errors
        return validate

    @classmethod
    def with_set(cls, res, ans):
        return cls.set(ans)(res)

    @classmethod
    def multiset(cls, seq):
        def validate(res):
            c1 = collections.Counter(seq)
            c2 = collections.Counter(res)
            for key in c2:
                if key not in c1 or c2[key] != c1[key]:
                    return False
                c1.pop(key)
            return not c1
        return validate

class ObjectDumper:

    @classmethod
    def matrix(cls, mx):
        print('[')
        for row in mx:
            print(' ', row)
        print(']')

