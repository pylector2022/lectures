#Lecture 01
##How you can find me 

**github**: pylector2022

**email**: python.lector.2022@gmail.com


##AGENDA

   1. Introduction
   2. Types
   3. Statements
   4. Helpful info

 ##1. Introduction
1. Why do you choose python?
2. What do you expect from python course?
3. What are your goals?
4. What are you willing to do to achieve your goals?


##2. Types
1. **Text Type**
```text
                 "Hello world"
                 'Hello world'
                 f'Hello world'
```
2. **Numeric Types**
```text
                 integer -> 1, 2, 5
                 float -> 0.43
                 complex -> 2 + j2
```


3. **Sequence Types**
```text
                 list > list(), [], [1, 2, 4, 5]
                 tuple > tuple(), (1, 2, 4, 5)
                 range > range(1, 6)
```

4. **Mapping Type**
```text
                 dict > dict(), {'key_1': 1, 1: 2}
```
5. **Set Types**
```text
                 set > set(), {1, 3, 4, 5}
                 frozenset > frozenset({1, 2, 3})
```
6. **Boolean Type**
```text
                 bool > bool(), True, False
```

7. **Binary Types**
```text
                 bytes > bytes(), b'bytes'
                 bytearray > bytearray(b'hello world!')
                 memoryview > memoryview(bytearray(b'hello world! '))
```

###Mutable and Immutable 
All types separate onto two gropes - mutable and immutable 
```text
    Mutable -> list, dict, set
    Immutable -> int,  float, complex, str, tuple, range, frozenset, bool, etc.
```


##2. Statements
1. Basic mathematical statements
```text
    +    2 + 2
    -    2 - 1
    *    2 * 3
    /    5 / 2
    //   5 // 2
    **   2 ** 3
    %    3 % 2
```
2. Logic and compare statements
```text
    and   True and False
    or    False or True
    not   not False
    is   True is True

    >    2 > 3
    <    4 < 5
    ==   4 == 4
    >=   5 >= 3
    <=   4 == 4
    !=   3 != 4
```
3. Binary statements
```text
    &	a & b	bitwise AND
    |	a | b	bitwise OR
    ^	a ^ b	bitwise XOR (exclusive OR)
    ~	~a	    bitwise NOT
    <<	a << n	bitwise left shift
    >>	a >> n	bitwise right shift
```
4. What is wrong with equal statement
Math
```text
    2 + 3 = 5
```
   

python equal sign

    a = 1
    b = 2
        1   2
    c = a + b

concatenation

    string1 = 'Hello'
    string2 = 'word!'
    string3 = string1 + ' ' + string2
    
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = list1 + list2
    
    tuple1 = (1, 2)
    tuple2 = (3, 4)
    tuple3 = tuple1 + tuple2

5. Condition expression

abstract condition expression
    
    if statement is true 
    then do this branch 
    else do this branch
    
    if 3 > 2 
    then say 2 is less than 3
    else 3 is less than 2
    
python condition expression
    
    if 3 > 2:
        print('2 is less than 3')
    else:
       print('3 is less than 2')


##4. Helpful info
How can I pass values into python code from terminal?
```python
a = int(input('Please, type value for a and press enter'))
b = int(input('Please, type value for b and press enter'))


# calculate perimeter of rectangle

result = (a + b) * 2


# How python can output data

print(result)
```