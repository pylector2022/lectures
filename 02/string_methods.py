"""
link: https://docs.python.org/3/library/stdtypes.html#string-methods
"""

c = "foo bar"

c.title().swapcase().format().center(30).swapcase()

print('=' * 30)

# Модифікатори
"foo bar".capitalize()
"foo bar".title()
"foo bar".upper()
'FOO BAR'.lower()


# Вирівнюваня
"foo bar".ljust(16, '_')
"foo bar".rjust(6, '~')
"foo bar".center(16, '~')
"foo bar".ljust(16)
"foo bar".rjust(16)
"foo bar".center(16)


# Видалення
"]>>foo ]>> bar<<[".lstrip("]>")
"]>>foo bar<<[".rstrip("<[")
"]>>foo bar<<[".strip("[]<>")
"  foo bar  ".strip()

# Розділення
"foo, bar".split(",")
"foo,,,bar".split(",")
"\t2 foo bar \r1\n ".split()
"foo,bar,baz".partition(",")
"foo,bar,baz".rpartition(",")


"foo.bar.baz.exe".rpartition(".")


# Об'єднання
"".join(["foo", "bar", "baz"])
", ".join(range(10))


# Перевірка на входження однієї строки в іншу
"foo" in "foobar"
"yada" not in "foobar"
"yada" in "foobar"

"foobar".startswith("foo")
"foobar".endswith(("boo", "bar"))

# Пошук підстроки в строці
# [1 3)
"abracadabra".find("ra")
"abracadabra".find("ra", 0, 3+1)
"abracadabra".index("ra", 0, 2+1)

try:
    a1 = "abracadabra".index("ra", 0, 3)
except ValueError as e:
    print('substr....')


# Заміна підстроки
"abracadabra".replace("ra", "**")
"abracadabra".replace("ra", "**", 1)
# множинна заміна

translation_map = {ord("a"): "bb", ord("b"): "aa"}
"abracadabra".translate(translation_map)

'abracadabra'.replace('a', 'b').replace('b', 'a')


# Предикати
"100500".isdigit()
"foo100500".isalnum()
"foobar".isalpha()
"foobar".islower()
"FOOBAR".isupper()
"Foo Bar".istitle()
"\r \n\t \r\n".isspace()

# Перетворення об'єкта в строку
str(1)
repr(1)
ascii("я строка")


class MyObject:
    a = 1

    def __repr__(self):
        return 'a = {}'.format(self.a)


class MyObject1:
    a = 1

# Форматування
"{1}, {0}, how are you?".format("Hello", "Sally", "Norton")
"{{}}, {1}, how are you?".format("Hello", "Sally")
"{0}, {name}, how are you?".format("Hello", name="Sally")

"{greeding}, {name}, how are you?".format(greeding="Hello", name="Sally")

"Today is October, {}th.".format(8)
"{!s}".format({1:1, 2:2}) # str
"{!r} is dict".format({1:1, 2:2}) # repr
"{!a}".format("я строка") # ascii


for key, value in {1:1, 2:2}.items():
    print(key, '=', value)

print("{!r} is dict".format({1:1, 2:2}))

"{:~^16} some text".format("foo bar")
"int: {0:d} hex: {0:x}".format(42)
"oct: {:o}".format(42)
"{:+08.2f}".format(-42.42)
"{!r:~^16}".format("foo bar")

"{0}, {1}, {0}".format("hello", "kitty")
"{0}, {who}, {0}".format("hello", who="kitty")

point = 0, 10
"x = {0[0]}, y = {0[1]}".format(point)

point = {"x": 0, "y": 10}
"x = {0[0]}, y = {0[1]}".format(point)

# old version
"%s, %s, how are you?" % ("Hello", "Sally")
"x = %(x)+2d, y = %(y)+2d" % point


# Модуль string
import string

string.ascii_letters
string.digits
string.punctuation
string.whitespace