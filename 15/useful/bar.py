from . import db
import foo


def my_print(*args, **kwargs):
    print(*args, **kwargs)


# if __name__ == '__main__':
my_print(foo.my_sum(1, 2, 3))