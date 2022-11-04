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