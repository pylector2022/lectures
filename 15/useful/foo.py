import bar
from . import db


def my_sum(*args):
    return sum(args)

bar.my_print('test')