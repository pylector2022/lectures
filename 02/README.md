# AGENDA
1. Boolean type and logic operations.
2. if-elif-else statements.
3. String type and string's methods.
4. Examples.


## 1. Boolean type and logic operations

### 1.1 Boolean type
    True
    False

Special type
    
    None

Convert any type to boolean type using bool() func.


Truthy values

    True
    int, float != 0
    len(string) > 0
    

Falsy values

    False
    None
    int, float == 0
    len(string) == 0
    [], {} (), set(), frozenset()

### 1.2. Logic operations
    
    and   True and False -> False
    or    False or True -> True
    not   not False  -> True
    is    True is True -> True

    >    2 > 3   -> False
    <    4 < 5   -> True
    ==   4 == 4  -> True
    >=   5 >= 3  -> True
    <=   4 <= 4  -> True
    !=   3 != 4  -> True

#### Grouping by brackets
```python

r1 = (True or False) and False
r2 = (not True and False) or True
r3 = (not True and False) or True
r4 = False or not (True and True)

r5 = (2 < 4) and (4 < 5)
r6 = (2 > 4) or (4 < 5)

r7 = (2 < 4) == 4
```

## 2. if-elif-else statements

Full statements

```python

if condition1:
    # this branch will be execute if condition1 is true
    ...
elif condition2:
    # this branch will be execute if condition2 is true
    ...
elif condition3:
    # this branch will be execute if condition2 is true 
    ...
else:
    # this this branch will be execute if all conditions are false
    ...
```

Short statements

```python
# Example 1
if condition1:
   # this branch will be execute if condition1 is true
   ...

# Example 2
if condition1:
    # this branch will be execute if condition1 is true
    ...
elif condition2:
    # this branch will be execute if condition2 is true
    ...

# Example 3
if condition1:
    # this branch will be execute if condition1 is true
    ...
elif condition2:
    # this branch will be execute if condition2 is true
    ...
elif conditionN:
    # this branch will be execute if condition2 is true 
    ...

# Example 4 
if condition1:
    # this branch will be execute if condition1 is true
    ...
else:
    # this this branch will be execute if all conditions are false
    ...
```
All possible combinations and nestings
```python
# Example 1
if condition1:
    if condition2:
        ...
    ...

# Example 2
if condition1:
    ...
else:
    if condition2:
        ...
    ...

# Example 3
if condition1:
    if condition2:
        ...
    ...
else:
    if condition3:
        ...
    ...
```
    
## 3. String type
```python
s1 = "This is a string"
s2 = 'This is a string too'

s3 = 'it\'s a good program'

s4 = """
it's a code
        test 
                test 1 {5 + 6}
"""

s5 = '''
it's a code
        test 
                test 1 {5 + 6}
'''
```

Concatenation of strings
```python
a = "This is"
b = ' '
c = 'a string'

# bag option
print(a + b + c)

# using another string and method join
''.join([a, b, c])
' '.join([a, c])

# using f-string 
f'{a}{b}{c}'
f'{a} {c}'
```

Convert another type to string using str func.
```python
number = 123
string_number = str(number)
print(string_number)

bool_value = True 
string_bool_type = str(bool_value) # string_bool_type = 'True'
print(string_bool_type)

string_bool_type = str(False)
print(bool(string_bool_type))
```

## 3.1 String's methods

1. [Official docs](https://docs.python.org/3/library/stdtypes.html#string-methods )
2. Examples in [string_methods.py](string_methods.py)

