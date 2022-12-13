import sys


def get_data_from_site(url):
    return '''<html>....'''


def div(i1, i2):
    if i2 == 0:
        raise ZeroDivisionError(f'We got var {i2=} !!!')
    return i1 / i2

a = 1
if not isinstance(a, (int, float)):
    raise TypeError(f'Got a {type(a)} expected int or float')



if a  < 0:
    raise ValueError(f'a should not be less 0')


class AppBaseError(Exception):
    pass


class MyCustomError1(AppBaseError):
    pass


class MyCustomError2(AppBaseError):
    pass


def main():
    try:
        print()
    except MyCustomError2 as err:
        print()

    raise MyCustomError1()


if __name__ == '__main__':

    try:
        main()
    except AppBaseError as err:
        print()

    except Exception as err:
        print()












    try:
        try:
            a = div(10, 2)
            print(f'{a=}')
            b = div(10, 0)
            print(f'{b=}')
            c = div(10, -2)
            print(f'{c=}')
        except ZeroDivisionError as err:
            print(err)
            b = 0
            c = 0
            raise err
            # raise Exception
    except Exception as err:
        print(err)
        raise err
    else:
        print(f'{a + b + c=}')
    finally:
        print('Done!')

"""


int main(void) {
    int a = 1
    int b = 2
    int c = a + b
    ...
    return 0    
}


"""











