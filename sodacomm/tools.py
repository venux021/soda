def testwrapper(func):
    def _test(*args, **kwargs):
        r = func(*args, **kwargs)
        print('----')
        return r
    return _test
