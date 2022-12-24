"""
 Dock string
"""
# STL built-in python libraries
import sys
import math
import itertools

# third-part libraries
import flask
import peewee

# own packages and libraries
import test_pack


# This is a comment
SOME_CONSTANT = 1
# This is a docs
ANOTHER_CONST = 2


var_1 = 122
var_2 = 455
a = 'this is a string'


def func_1(a, b):
    """
    Desc
    :param a:
    :param b:
    :return:
    """
    return a / b


def table_exists(table: str, schema=None):
    """
    Bind the given list of models, and specified relations, to the database.
    :param table (str):
    :param schema (str):
    :return bool:
    """
    return True


def func2():
    return 42


class Circle:
    """

    """
    def get_perimeter(self):
        """
        calculate and return perimeter
        :return perimeter (int):
        """
        perimeter = 100
        return perimeter


# Comments
test = Circle.__name__
new_class = type('NeClass', (Circle, ), {'get_perimeter': func2})


class B(Circle):
    ...


def main():
    """

    :return:
    """
    circle = Circle()


if __name__ == '__main__':
    main()


