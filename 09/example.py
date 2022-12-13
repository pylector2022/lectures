class A(object):
    attr = 42



def method_of_class(self, *args, **kwargs):
    print(*args, kwargs)


name_c, bases_c, attrs_c = 'C', (), {'print':  method_of_class}



class Meta(type):
    def some_method(cls):
        return 45

class Test(metaclass=Meta):
    attr = 60

    def __new__(cls, *args, **kwargs):
        ...

    def __init__(self):
        ...

test = Test()

class dict:
    @classmethod
    def fromkeys(cls, list_):
        obj = cls()
        return obj.update({key: None for key in list_})

    @staticmethod
    def test():
        print()





import abc


class Figure(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_perimeter(self):
        pass

    @abc.abstractmethod
    def get_area(self):
        pass


class Circle(Figure):
    def get_perimeter(self):
        return 1000



# LEGB
# public
# protected
# private

'''

class MyTestClass:
    public a = 10
    protected b = 10
    private c = 10

class B(MyTestClass)

    def test(self):
        self.b = 10
        self.c = 90


test = MyTestClass()
print(test.a) 

'''

class MyTestClass:
    a = 10
    _b = 10
    __c = 10

    def public(self):
        print(1)

    def _protected(self):
        print(2)

    def __private(self):
        self.__private()
        print(3)




































