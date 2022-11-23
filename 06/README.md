# AGENDA
1. Function and keywords
2. While statement
3. Decorator & functools


## 1. Function and keywords

```python

def func1(*args, **kwargs):
    print(f'{args=} {kwargs=}')

args = (1, 2, 3)
kwargs = {
    'arg1': 1,
    'arg2': 2,
}

func1(*args, **kwargs)

```

## 2. While statement

```python
i = 1
while True:
    s = a + b
    if i == 4:
        continue
    if i == 5:
        break
    print(f'{i=}')
else:
    print('You will see this message if while wouldn"t stop by break operator')
```

##3. Decorator & functools


