### AGENDA

1. List and tuple
2. for-else 
3. Unpacking
4. range, enumerate, min, max, sum 


## List and Tuple

![](./img/151a4791320407e8b302d404af4.jpeg)

### List
```python
# index   =>  0   1   2   3   4   5
my_list_1 = [10, 20, 30, 40, 50, 60]

my_list_2 = []
my_list_3 = list()
```    

#### Methods

```python

my_list_1 = [10, 20, 30]
my_list_2 = [40, 50, 60]

x = 2
i = 1

my_list_1.index(x)         # Повертає положення першого елемента зі значенням x
my_list_1.count(x)         # Повертає кількість елементів зі значенням x

my_list_1.append(x)        # Додає елемент в кінець списку
my_list_1.extend(my_list_2)    # Розширює список my_list_1, додаючи в кінець все елементи списку list2
my_list_1.insert(i, x)     # В ставлять на i-ий елемент значення x
my_list_1.remove(x)        # Видаляє перший елемент у списку, який має значення x. ValueError, якщо такого елемента не існує
my_list_1.sort()           # Сортує список на основі функції
my_list_1.reverse()        # Розгортає список
my_list_1.clear()          # Очищає список
my_list_1.pop(i)           # Видаляє i-ий елемент і повертає його. Якщо індекс не вказано, видаляється останній елемент

my_list_1.copy()           # Поверхнева копія списку
```


### Tuple

tuple1 = (1, 2, 3, 4, 5, 6, 4)
tuple2 = tuple()

tuple3 = 1, 2, 3, 4, 5
tuple4 = (1, )


#### Methods

```python

tuple1 = (1, 2, 3, 4)

tuple1.index(2)  # шукає заданий елемент у кортежі та повертає його позицію. Він повертає перше входження елемента в кортеж.
tuple1.count(4)  # повертає кількість, скільки вказаний елемент з’являється в кортежі.

```

```python

list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_of_tuple = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

tuple_of_list = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
tuple_of_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

...
```

convert tuple into list and list into tuple
```python
l1 = [1, 2, 3, 4]
t1 = 1, 2, 3, 4

t2 = tuple(l1)
l2 = list(t1)
```

concat tuples or list
```python
t1 = 1, 2, 3
t2 = 4, 5, 6
t3 = t1 + t2

l1 = [5, 6, 7]
l2 = [8, 9, 0]
l3 = l1 + l2

```


## For-else statement

```python
list1 = [1, 2, 3, 4, 5, 6]

# option 1
for item in list1:
    print(item)

# option 2
for item in list1:
    if item == 4:
        continue
    print(item)
    
# option 3
for item in list1:
    if item == 4:
        continue
    if item == 5:
        break
    print(item)
    

# option 4
for item in list1:
    if item == 4:
        continue
    print(item)
else:
    print('Printed by else branch')
```


## Unpacking
```python
tuple1 = (1, 2, 3)
a, b, c = tuple1

list1 = [1, 2, 3, 4, 5, 6]
a, *b, c = list1

list2 = [(1, 3), [2, 4], (5, 7), (6, 8)]
a, *b, c = list2


list3 = [1, 2, 3]
a, *b = list3
*a, b = list3

# errors
a, b, c, d = list3
*a = list3


a = 1
b = 2

a, b = b, a

```
   

#### Where it should be used?

```python

for item in [(1, 2), (3, 4), (5, 6)]:
    a, b = item
    print(a + b)


for a, b in [(1, 2), (3, 4), (5, 6)]:
    print(a + b)

```


## 4. range, enumerate, min, max, sum

### Range

[range doc 1](https://docs.python.org/3/library/functions.html#func-range)

[range doc 2](https://docs.python.org/3/library/stdtypes.html#range)


range(start, stop, step)

```python
list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(0, 30, 5))
# [0, 5, 10, 15, 20, 25]
list(range(0, 10, 3))
# [0, 3, 6, 9]
list(range(0, -10, -1))
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
list(range(0))
# []
list(range(1, 0))
# []
```

### enumerate

enumerate(sequence, start=0)

```python
l1 = ['test1', 'test2', 'test3']

for index, item in enumerate(l1, 1):
    print(index, item)

    
index = 1
for item in l1:
    print(index, item)
    index = index + 1


```

### min, max, sum 

min(sequence)
max(sequence)
sum(sequence)

```python
l1 = [1, 2, 3, 4, 5]
min(l1)
max(l1)
sum(l1)
```