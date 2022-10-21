import math

input_str = input()

values=input_str.split()
count =len(values)

if count == 1:
    a = int(''.join(values))
    if a == 0:
        print('There can\'t be a circle with 0 radius')
    else:
        print(f'circle: radius = {a}; perimeter = {2*a*3.14}; area = {3.14*a**2}')
elif count == 2:
    a1, b1 = values
    a = int(''.join(a1))
    b = int(''.join(b1))
    if a == 0 or b == 0:
        print('There can\'t be a square or a rectangle with 0 side')
    else:
        if a == b:
            print(f'square: side = {a}; perimeter = {a*4}; area = {a**2}')
        else:
            print(f'rectangle: side a = {a}; side b = {b}; perimeter = {(a+b)*2}; area = {a*b}')
elif count == 3:
    a1, b1, c1 = values
    a = int(''.join(a1))
    b = int(''.join(b1))
    c = int(''.join(c1))
    if a == 0 or b == 0 or c == 0:
        print('There can\'t be a triangle with 0 side')
    elif a + b < c or a + c < b or b + c < a:
        print('There can\'t be a triangle where sum of 2 sides is less than the 3-rd one')
    else:
        print(f'triangle: side a = {a}; side b = {b}; side c = {c}; perimeter = {a+b+c}; area = {math.sqrt(((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))}')




#  імпортували бібіотеку
import math


# Функція підійме виключення якщо хоча б один із елементів менший або дорівнює нулю
def validate_values(values):
    if not all(map(lambda item: int(item) <= 0, values)):
        raise ValueError('Passed values contain 0 or less 0')


# функція розраховує усе що потрідно для даної фігури, в майбутньому її легко перетворити на клас.
def calculate_triangle(values):
    a, b, c = map(int, values)
    # додаткова перевірка саме для трикутника
    if a + b <= c or b + c <= c or a + c <= 0:
        raise ValueError(f'Triangle cannot be possible with passed values {values=}')
    perimeter = a + b + c
    half_perimeter = perimeter / 2
    square = math.sqrt(half_perimeter*(half_perimeter-a)*(half_perimeter-b)*(half_perimeter-c))
    return f'Triangle: {a=} {b=} {c=} {perimeter=} {square}'


# функція розраховує усе що потрідно для даної фігури, в майбутньому її легко перетворити на клас.
def calculate_rectangle(values):
    a, b = map(int, values)
    perimeter = (a + b) * 2
    square = a * b
    type_ = 'Square' if a == b else 'Rectangle'
    return f'{type_}: {a=} {b=} {perimeter=} {square}'


# функція розраховує усе що потрідно для даної фігури, в майбутньому її легко перетворити на клас.
def calculate_circle(radius_str):
    radius = int(radius_str)
    perimeter = 2 * a * math.pi
    square = math.pi * a ** 2
    return f'Circle: {radius=}; {perimeter=} {square}'


# отримуємо значення, одна точка введення даних
input_str = input()
# розбиваємо на частини
values = input_str.split()
# перевіряємо корректність даних
validate_values(values)
# рахуємо кількість
count = len(values)
# в залежності від кількості викликаємо відповідну функцію
if count == 3:
    res = calculate_triangle(values)
elif count == 2:
    res = calculate_rectangle(values)
elif count == 1:
    res = calculate_circle(values)
else:
    # додаткова перевірка якщо кількість переданих даних завелика
    raise ValueError(f'Passed unexpected count of values, {count=}')
# виводимо дані, одна точка виводу даних.
print(res)
