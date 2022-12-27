from dataclasses import dataclass



class A:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


obj_a = A(1, 2, 3, 4)

print(obj_a.__dict__)

import typing


@dataclass
class B:
    a: int
    b: int
    c: int



obj_b = B(1, 2, 3, 'test')
print(obj_b.__dict__)


@dataclass
class Point:
     x: int
     y: typing.Any



@dataclass
class C:
     mylist: list[Point]



pa = Point(1, 2,)
pb = Point(1, 2,)

r = pa.y + pb.x


# l = [point_a, point_b]
l = [None, None]

c = C(l)

