import functools
import sys
import typing


def tracer(file=sys.stdout):
    def call(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            print(f'{args=} {kwargs=} {res=}', file=file)
            return res
        return inner
    return call


class Test1:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        res = self.func(*args, **kwargs)
        print(f'{args=} {kwargs=} {res=}')
        return res


class Test2:
    def __init__(self, file=sys.stdout):
        self.file = file

    def __call__(self, func: typing.Callable):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            print(f'{args=} {kwargs=} {res=}', file=self.file)
            return res
        return inner


@tracer(file=sys.stderr)
def test1(a, b):
    return a + b

@Test1
def test2(a, b):
    """
    This is a test 2 func
    :param a:
    :param b:
    :return:
    """
    return a + b


@Test2(file=sys.stderr)
def test3(a, b):
    """
    This is a test 2 func
    :param a:
    :param b:
    :return:
    """
    return a + b



class A:
    a = 1
    perimeter = 1
    formatted_data = 1

    def __init__(self):
        self.type = self.__class__.__name__

    def format_data(self):
        self.formatted_data = 109

    def друкувати(self):
        print(self.a)

    def отримати_тип(self):
        return self.type

    def чи_файл_відкритий(self):
        return True

if __name__ == '__main__':
    # # test1(11, 21)
    # test2(10, 20)

    µћґљќ = A()
    µћґљќ.друкувати()



class Figure:
    ...


class CircleFigure(Figure):
    ...




class ArticleModel:
    ...


class ArticleView:
    ...


