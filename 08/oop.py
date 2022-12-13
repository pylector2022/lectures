"""
ООП

Інтерфейс
=>
Клас
=>
Обʼєк



Клас             Обʼєкт(Екземпляр Класу)    Обʼєкт(Python)
поля даних  =>   властивості             => атрибут
методи      =>   поведінка               => атрибут
"""


class Book:
    # поле
    type = 'magazine'

    # метод
    def __init__(self, name, author):
        self.author = author
        self.name = name

    # метод
    def get_author(self):
        return self.author

    # метод
    def get_name(self):
        return self.name


book = Book('John', 'Math')
print(book.type)
print(book.get_author())



"""
Принципи ооп

1. Абстакція
2. Інкапсуляція
3. Наслідування
4. Поліморфізм


Абстакція
Інкапсуляція
Наслідування
Поліморфізм


"""

def div(a, b):
    return a / b


res = div(10, 3)


class A:
    def test(self):
        return 43


class B(A):
    def test2(self):
        return self.test() / 3



class Client:
    def get(self, site):
        response = send_request(site)
        return response.text


class ClientBBC(Client):
    site = 'bbc.com'

    def get(self, site):
        result = super().get(self.site)
        return result


# Інтерфейс
class Figure:
    def get_perimeter(self):
        raise NotImplementedError()

    def get_area(self):
        raise NotImplementedError()

class NonNegative:
    

# Класс Triangle реалізує інтерфейс Figure
class Triangle(Figure):
    a = NonNegative()
    b = NonNegative()
    c = NonNegative()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if self.a + self.b <= self.c or ...:
            raise MyCustomError('')

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        return ...
