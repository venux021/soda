import functools
import time

__test_number = 0

def execute(func, args, kwargs, *, show_args=True, show_result=True):
    global __test_number
    __test_number += 1
    print(f'**[{__test_number}]**')
    if show_args:
        if args:
            print('args:', args)
        if kwargs:
            print('kwargs:', kwargs)
    t1 = time.time()
    res = func(*args, **kwargs)
    t2 = time.time()
    if show_result:
        print(f'result:', res)
    print(f'----')
    print(f'{(t2-t1)*1000:.3f} ms\n')
    return res

def simpletest(func):
    @functools.wraps(func)
    def _test(*args, **kwargs):
        return execute(func, args, kwargs, show_args=False, show_result=False)
    return _test

testwrapper = simpletest

def sodatest(repeat=1,show_args=True,show_result=True):
    def _wrapper(func):
        @functools.wraps(func)
        def runner(*args, **kwargs):
            for i in range(max(1,repeat)):
                res = execute(func, args, kwargs, show_args=show_args, show_result=show_result)
            return res
        return runner
    return _wrapper

def testrun(func, *args, **kwargs):
    execute(func, args, kwargs)
