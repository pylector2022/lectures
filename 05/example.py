"""
min(a, /, *args)

min(1, 2, 4, 5, 6, -67, 0) == 0

"""


# def min(first, *args):
#     res = float('inf')
#     for item in (first, ) + args:
#         if item < res:
#             res = item
#     return res


"""

min(1, 2, 4, 5, 256, -67, 0, lo=0, hi=255) == 0
min(1, 2, 4, 5, 256, -67, 0) == 0

min(-5, 12, 13, lo=0, hi=255) == 12

"""


# def min(first, *args, lo=float('-inf'), hi=float('inf')):
#     res = hi
#     for item in (first, ) + args:
#         if item < res and lo < item < hi:
#             res = item
#     return max(res, lo)



Local
E
G
B

# build-in
set = {1, 2, 3, 4}

set()


# global
a = 1
b = 2
d = 1

def test():
    # local
    d = 10
    c = a + b + d
    print(f'{c} = {a} + {b} + {d}')

# global
b = 12
b = 14
def test101():
    c = 10

    min(10, 10, 10,)
    def main_inner():

        def min(first, *args, lo=float('-inf'), hi=float('inf')):
            res = hi
            for item in (first,) + args:
                if item < res and lo < item < hi:
                    res = item
            return max(res, lo)

        d = 10
        def inner():
            # local
            a = 10
            return min(a, b, c, d, lo=2, hi=10)

        inner()




a = a + 1





# LEGB
value = 100

def cell(value=None):

    def _get():
        return value

    def _set(input_value):
        nonlocal value
        value = input_value

    return _get, _set

get1, set1 = cell(10)








def l_func(a, b, c):
    if a == 0:
         return a
    else:
        if b == 0:
            return b
        else:
            return c



l_func = lambda a, b, c: a.append([b, c])


res = l_func(0, 1, 10)



map(func, [1, ,])


def compare(a):
    return a >= 0

