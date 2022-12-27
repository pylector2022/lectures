"""
This is a simple module.
"""
import argparse
from sys import path


CONST1 = 10
some_var = 12


def test(a, b):
    """ This is a func"""
    return a + b


def my_sum(*args, **kwargs):
    return sum(args, **kwargs)


def main():
    print(CONST1 + some_var)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))
