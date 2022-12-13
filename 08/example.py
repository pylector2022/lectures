#
import sys


def check(a):
    return a > 0

class Test:
    a = Desct()

    def __init__(self, b):
        if not check(b):
            self.b = b
        else:
            print('Error', file=sys.stderr)

a = 0

test = Test(10)
test.b = a
test.a = a

class Math:

    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            print('Error', file=sys.stderr)






class NonNegative:
    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        assert value > 0, 'non-negative value required'
        setattr(instance, self.name, value)





class Test1:
    value1 = NonNegative()
    def __init__(self, a):
        self.value1 = a
        print(self.value1)
        print( 10 + self.value1)



test1 = Test1()
test1.value1




class A:
    b = property()


class C(object):
    @property
    def x(self):
        "I am the 'x' property."
        return self._x

    @x.setter
    def x(self, value):
        self._x = value



c = C()

c.x = 10

def test(a, b)
    return a + b

test(c.x(), 2)


map(int, '1234')



class Book:
    def __init__(self, name):
        self.name = name

    @property
    def readers(self):
        return get_from_db_all_readers(self.name)



book = Book('Math')
book.readers # => ['John Dou', '...']
