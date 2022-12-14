"""
Є рядок що містить числа розділені пробілами, який може мати наступні варіанти

input_str1 = '10 20'
input_str2 = '10 20 30'
input_str3 = '10'
В залежності від кількості чисел визначити тип фігури

10 20 -> прямокутник або квадрат
10 20 30 -> трикутник
10 -> круг (вказано радіус)
Для кожної фігури порахувати периметр та площу та вивести в наступному форматі

тип: сторона1=10, сторона2=20; периметр = 345, площа = 234
приклад

triangle: a = 10, b = 20, c = 30; perimeter = 1234, square = 567
Увага! Рядок може містити дані, які суперечать існуванню фігури.
"""

input_string = input()
values = input_string.split()

count = len(values)
if count == 1:
    r = int(input_string)
    if r <= 0:
        print('Такий круг не може існувати')
    else:
        s = ...
        p = ...
        print(f'Circle: {r=}; {s=} {p=}')
elif count == 2:
    a, b = values
    a1 = int(a)
    b1 = int(b)
    if a1 <= 0 or b1 <= 0:
        print('Такий прямокутник не може існувати')
    else:
        s = ...
        p = ...
        print(f'Rectangle: {a=} {b=}; {s=} {p=}')
elif count == 3:
    a, b, c = values
    a1 = int(a)
    b1 = int(b)
    c1 = int(c)
    if a1 <= 0 or b1 <= 0 or c1 <= 0:
        print('Такий трикутник не може існувати')
    elif a1 + b1 <= c1 or c1 + b1 <= a1 or a1 + c1 <= b1:
        print('Такий трикутник не може існувати')
    else:
        s = ...
        p = ...
        print(f'Triangle: {a1=} {b1=} {c1=}; {s=} {p=}')




