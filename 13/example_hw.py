import sys
ENABLE_TRACE = True # False


def super_trace(file=...):
    ...


@super_trace(file=sys.stderr)
def test1(a, b, c):
    return [a, b, c], a, str(b), float(c)


@super_trace()
def test2(a, b, *, c, d):
    return [a, b, c, d], a, str(b), float(c), d


@super_trace(file=sys.stderr)
def test3(*, a, b, c, d):
    return [a, b, c, d], a, str(b), float(c), d


@super_trace()
def test4(a, b, *, c, d):
    print([a, b, c, d], a, str(b), float(c), d)


@super_trace()
def test5():
    return [1, 2, 3]



if __name__ == '__main__':
   # test ENABLE_TRACE = False
   ENABLE_TRACE = False
   test1(1, 2, 3)
   test2(1, 2, c=3, d=4)
   test3(a=1, b=2, c=3, d=4)
   test4(1, 2, c=3, d=4)
   test5()

   # test ENABLE_TRACE = True
   ENABLE_TRACE = True
   test1(1, 2, 3)
   test2(1, 2, c=3, d=4)
   test3(a=1, b=2, c=3, d=4)
   test4(1, 2, c=3, d=4)
   test5()