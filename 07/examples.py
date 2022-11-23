class NameOfClass:
    pass


a = NameOfClass()


class NameOfClass:
    def test_func(self):
        return 42


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self, *, k=1):
        return (self.a + self.b) * 2 + k

    def area(self):
        return self.a * self.b


rec1 = Rectangle(10, 20)
print(rec1.area())
print(rec1.perimeter(k=2))

str1 = str(1234)
str1.replace('3', 'e')



class Test:
    def show_self(self):
        print(f'{type(self)=}')
        print(f'{dir(self)=}')
        print(f'{repr(self)=}')

    def return_self(self):
        return self

Test.show_self()

test = Test()

test.show_self(test)




class Car:
    def __new__(cls, *args, **kwargs):
        obj = cls()
        # list1.sort()
        obj.__init__(*args, **kwargs)
        return obj

    def __init__(self, color):
        self.color = color
        self.is_engine_working = False
        self.vin = id(self)

    def get_color(self):
        return self.color

    def start_engine(self):
        self.is_engine_working = True

    def get_vin(self):
        return self.vin

    def stop_engine(self):
        self.is_engine_working = False


bmw = Car.__new__('red')



audi = Car('black')
audi.start_engine()
audi.get_vin()






def test():
    return 1


t = test()



a = 10
b = 20



def perimeter(a, b):
    return (a + b) * 2


def area(a, b):
    return a * b



p1 = perimeter(a, b)
a1 = area(a, b)

def print_rec(a, b, p1, a1):
    print(f'{a=} {b=}, {p1=}, {a1=}')










class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.perimeter = self.__perimeter()
        self.area = self.__area()

    def __perimeter(self):
        return (self.a + self.b) * 2

    def __area(self):
        return self.a * self.b



rec1 = Rectangle(10, 20)
rec1.area
rec1.perimeter

rec1.a = 11
rec1.b = 12
rec1.area
rec1.perimeter







class Rectangle:
    """
    This is class that contains info about rectangle
    """
    c = 10

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2 + self.c

    def area(self):
        return self.a * self.b

    def __str__(self):
        return f'Rectangle a={self.a} b={self.b}'

rec1 = Rectangle(10, 20)

variables = raw_input.split()

if len(variables) == 2:
    rec1 = Rectangle(*variables)
    print(rec1)


variables = raw_input.split()

def calc_obj(*args):
    #1. rectangle, triangle, circle
    #2. calc area, perimeter
    #3. print(result)
    ...

    if len(args) == 2:
        rec1 = Rectangle(*args)
        print(rec1)



def test():
    ...



class Bottle:



