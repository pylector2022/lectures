# AGENDA
1. Function
2. LEGB
3. Lambda
4. map, filter


## FUNCTION

```python
def name_of_function(variable1, variable2, variable3):
    res = (variable1 + variable2) / variable3
    return res


def func(a, b, c):
    sum1 = a + b
    return sum1 / c  # return (sum1 / c)


def func2(a, b):
    sum1 = a + b
    print(f'{sum1=}')
    # return None


def func3(*args):
    print(f'{args=}')
    return sum(args)


def func4(a, *args, b):
    print(f'{a=}')
    print(f'{args=}')

    
def func5(a, b, /, c, d):
    return (d * (c + b))/ a


def func6(a, b, *, c, d):
    print(a, b, c, d)
    

def func7(a, b, *, /, c, d):
    print(a, b, c, d)


def func8(a, b, /, d, c=1):
    return a + b + c + d




def func9(a, f=[]):
    f.append(a)
    print(f)
    

func9(1)

1. __f = []
2. f = __f

def func10(a, f=None):
    f = f or []
    f.append(a)
    return f


func10(1, 4)
```

any_1, all_1, zip_1, map, filter, sum, enumerate, range

zip_1 == list(zip())



all([]) == your_all([])
all([True, False]) == your_all([True, False])
all([True, True]) == your_all([True, True])
all([False, False]) == your_all([False, False])

any([]) == your_any([])
any([True, False]) == your_any([True, False])
any([True, True]) == your_any([True, True])
any([False, False]) == your_any([False, False])

list(zip(range(10), range(15), range(8))) == your_zip(range(10), range(15), range(8))
list(zip(range(10), range(15), [])) == your_zip(range(10), range(15), range(8))
list(zip(range(10))) == your_zip(range(10))

list(map(int, '1234567890')) == your_map(int, '1234567890')
list(map(min, range(10), range(20, 30), range(25, 15, -1))) == your_map(min, range(10), range(20, 30), range(25, 15, -1))

list(filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False])) == your_filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False]) 
list(filter(lambda a: a % 2 == 0, range(10+1))) == your_filter(lambda a: a % 2 == 0, range(10+1))


sum(range(10)) == your_sum(range(10))
sum([]) == your_sum([])

list(enumerate('1234567890', 1)) == your_enumerate('1234567890', 1)

list(range(10)) == your_range(10)
list(range(10, 20)) == your_range(10, 20)
list(range(10, 20, 3)) == your_range(10, 20, 3)
list(range(20, 10, 3)) == your_range(20, 10, 3)
list(range(20, 10, -3)) == your_range(20, 10, -3)
list(range(20, 10)) == your_range(20, 10)