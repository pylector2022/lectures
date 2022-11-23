import functools
import sys

TRACE_PRINT = True


def trace(*, file=sys.stdout):
    print('1')
    def deco(func):
        print('    2')
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if TRACE_PRINT:
                print(func.__name__, args, kwargs, file=file)
            return func(*args, **kwargs)
        return inner
    return deco


def trace(func=None, *, file=sys.stdout):
    if func is None:
        def deco(func):
            return trace(func, file=file)
        return deco

    @functools.wraps(func)
    def inner(*args, **kwargs):
        if TRACE_PRINT:
            print(func.__name__, args, kwargs, file=file)
        return func(*args, **kwargs)
    return inner


@trace(file=sys.stderr)
def test(a, b, *, zero=1):
    if b == 0:
        return a / zero
    return a / b


print(test(10, 0, zero=5))









# deco = trace(file='This a file')
# deco('This is a func')

# print('-' * 60)
# inner = trace(2)
# inner(1,2,3, test=1)





# res = test(10, 0, zero=5)
# print(res)

