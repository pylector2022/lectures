# __iter__
# __next__


class MyIterator:
    def __init__(self, max):
        self.__coll = list(range(max))
        self.id = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            res = self.__coll[self.id]
        except IndexError:
            raise StopIteration
        self.id += 1
        return res

    def __contains__(self, item):
        return item in self.__coll


my_iter = MyIterator(10)
print(3 in my_iter)




# __getitem__

class MyIterator2:
    def __init__(self, num):
        self.num = num
    def __getitem__(self, item):
        if item > self.num:
            raise IndexError
        return item


print(list(MyIterator2(10)))

my_it = MyIterator2(10)

def list(my_it):
    res = []
    for index in range(int('inf')):
        res.append(my_it.__getitem__(index))
    return res




class TextIterator:
    def __init__(self, text):
        self.iter = iter(text.split())

    def __iter__(self):
        return self

    def __next__(self):
        el = next(self.iter)
        el = el.replace('a', '_')
        return el


text = """
If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default
"""
ti = TextIterator(text)





def g():
    print('Started')
    x = 1
    yield x
    x += 1
    yield x
    print('Done')
    return 'This is a message'





def unique(iterable, seen=None):
    seen = set(seen or [])
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


xs = [1, 1, 2, 3, 4, 5]

list(unique(xs))


def g2():
    for item in range(10):
        yield item ** 2




def g2():
    print('Start')
    res = yield
    print('Got {!r}'.format(res))
    res = yield 42
    print('Got {!r}'.format(res))
    print('Stop')




def grep(pattern):
    print(f'Looking for {pattern=}')
    while True:
        try:
            text = yield
            if pattern in text:
                print('Pattern was found')
            else:
                print('Pattern wasn\'s found')
        except Exception as err:
            if isinstance(err, ValueError):
                break





def g():
    print('Start')
    yield 42
    yield 42
    yield 42
    yield 42



raise GeneratorExit()



def g1():
    yield 123
    return []


def g2():
    res = yield from g1()
    print('Got {!r}'.format(res))




import os
from contextlib import contextmanager

@contextmanager
def cd(path):                   # __init__
    previous_path = os.getcwd() # __enter__
    os.chdir(path)              # __enter__
    try:                        # __enter__
        yield                   # _________
    finally:                    # __exit__
        os.chdir(previous_path) # __exit__

res = []
for item in range(10):
    res.append(item ** 2)

res = [item ** 2 for item in range(10)]



res = []
for item in range(10):
    if item % 2 == 0:
        res.append(item ** 2)
    else:
        res.append(item ** 3)


res = []
for item in range(10):
    tmp = item ** 2 if item % 2 == 0 else item ** 3


res = [item ** 2 if item % 4 == 0 else item ** 3 for item in range(100) if item % 2 == 0 ]
print(res)

res = []
for item in range(10):
    if item % 2 == 0:
        res.append(item ** 2)

res = [item ** 2 for item in range(10) if item % 2 == 0]
print(res)


res = tuple([item ** 2 for item in range(10) if item % 2 == 0])
print(res)



class Figure:
    p = 0
    sizes = []
    def calc(self):
        self.p = sum(self.sizes)


## import figure


class PrintMixin:
    def show_table(self):
        ...

    def sqrt(self):
        ...

    def print(self):
        self.show_table()
        print(f'{self.p=}')


class PrintMixin2:
    def print(self):
        ...


class Triangle(Figure, PrintMixin2, PrintMixin1):
    def __init__(self, a, b, c):
        self.sizes = [a, b, c]


tri = Triangle(1, 2, 3)
tri.print()

class Rectangle(Figure, PrintMixin):
    def __init__(self, a, b):
        self.sizes = [a, b, a, b]
















