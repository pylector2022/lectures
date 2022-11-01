
# AGENDA

1. any, all, zip, sorted, reversed, len
2. Dictionary
3. Set and frozenset
4. Function. Basic.



## 1. any, all, zip, sorted, reversed, len

### any(iterable, /)
    
    Повертає True, якщо будь-який елемент iterable є true. Якщо iterable порожній, повертає False.

### all(iterable, /)
    
    Повертає True, якщо всі елементи iterable є true (або якщо iterable порожній).

### zip(*iterables, strict=False)
    
    Виконує ітерацію кількох ітерацій паралельно, створюючи кортежі з елементом з кожного.


### sorted(iterable, /, *, key=None, reverse=False) # list.sort()
    
    Повертає новий відсортований список з елементів у iterable. 
    Має два необов’язкові аргументи, які необхідно вказати як аргументи ключового слова.
    key визначає функцію одного аргументу, яка використовується для отримання ключа порівняння з кожного елемента 
    в iterable (наприклад, key=str.lower). 
    Значення за замовчуванням — Немає (порівняйте елементи безпосередньо).
    reverse — логічне значення. Якщо встановлено значення True, елементи списку сортуються так, ніби кожне порівняння було зворотним.

### reversed(seq) # list.reverse()

    Повертає зворотний ітератор. seq має бути об’єктом, який має метод __reversed__() 
    або підтримує протокол послідовності (метод __len__() і метод __getitem__() 
    з цілими аргументами, починаючи з 0).

### len(s) 

    Повертає довжину (кількість елементів) об’єкта. 
    Аргументом може бути послідовність (наприклад, рядок, байти, кортеж, список або діапазон) 
    або колекція (наприклад, словник, набір або заморожений набір).



## 2. Dictionary

```python

dict_1 = {}
dict_2 = dict()
dict_3 = {1: 3, 2: 5, 3: 6}
dict_4 = {
    'text_key1': 'text_value1',
    'text_key2': 'text_value2',
}

list_of_keys = ['key1', 'key2', 'key3']
dict5 = dict.fromkeys(list_of_keys, 'default_value')

list_of_keys = ['key1', 'key2', 'key3']
list_of_value = ['value1', 'value2', 'value3']
dict6 = dict(zip(list_of_keys, list_of_value))


```
### Methods

dict1.clear()                           # очищує словник.
dict1.copy()                            # повертає копію словника.
dict1.get(key1)                         # повертає значення ключа, але якщо його немає,
                                        # не кидає виняток, а повертає default (за замовчуванням None).
                                        
dict1.items()                           # повертає пари (ключ, значення).
dict1.keys()                            # повертає ключі у словнику.
dict1.pop(key1)                         # видаляє ключ і повертає значення.
                                        # Якщо немає ключа, повертає default (за замовчуванням кидає виняток).
                                        
dict1.popitem()                         # видаляє та повертає пару (ключ, значення).
                                        # Якщо словник порожній, кидає виняток KeyError.

dict1.setdefault(key1, default_value)   # повертає значення ключа, але якщо його немає,
                                        # не кидає виняток, а створює ключ зі значенням default (за замовчуванням None).
                                        
dict1.update(dict2)                     # оновлює словник, додаючи пари (ключ, значення) з dict2.
                                        # Існуючі ключі перезаписуються. Повертає None (не новий словник!). 


dict1.values()                          # повертає значення у словнику.       


dict.fromkeys(collection1, value)       # створює словник із ключами з collection1 і значенням value (за замовчуванням None).



## 3. Set and frozenset

```python
empty_set = set()
set1 = {1, 3, 4, 5, 5, 5}

list1 = [1, 2, 2, 2, 3, 3]
set2 = set(list1)
```

### Methods
Ці методи доступні для set і frozenset

set1.isdisjoint(set2)                   # істина, якщо set1 та set2 не мають спільних елементів.
set1 == set2                            # усі елементи set1 належать set2, всі елементи set2 належать set.
set1.issubset(set2)                     # або set1 <= set2 - усі елементи set1 належать set2.
set1.issuperset(set2)                   # або set1 >= set2 – аналогічно.
set1.union(set2, ...)                   # чи set1 | set2 | ... - об'єднання кількох множин.
set1.intersection(set2, ...)            # або set1 & set2 & ... - перетин.
set1.difference(set2, ...)              # або set1 - set2 - ... - множина з усіх елементів set, що не належать жодному з set2.
set1.symmetric_difference(set2)         # set1 ^ set2 - безліч з елементів, що зустрічаються в одній множині, але не зустрічаються в обох.
set1.copy()                             # копія множини.
set1.update(set2, ...)                  # set1 | = set2 | ... – об'єднання.
set1.intersection_update(set2, ...)     # set1 & = set2 & ... - перетин.
set1.difference_update(set2, ...)       # set1 -= set2 | ... - віднімання.
set1.symmetric_difference_update(set2)  # set1 ^= set2 - безліч з елементів, що зустрічаються в одній множині,
                                          але не зустрічаються в обох.

Ці методи доступні тільки для set

set1.add(elem)                          # додає елемент у set.
set1.remove(elem)                       # видаляє елемент із множини. KeyError, якщо такого елемента немає.
set1.discard(elem)                      # видаляє елемент, якщо він знаходиться у множині.
set1.pop()                              # видаляє перший елемент із множини. Так як множини не впорядковані,
                                        # не можна точно сказати, який елемент буде першим.
                                          
set1.clear()                            # очищення множини.


# 4. Function. Basic.

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


def func4(a, *args):
    print(f'{a=}')
    print(f'{args=}')

    
def func5(a, b, /, c, d):
    return (d * (c + b))/ a


def func6(a, b, *, c, d):
    print(a, b, c, d)
    

def func7(a, b, *, /, c, d):
    print(a, b, c, d)

```