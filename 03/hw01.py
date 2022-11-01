tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)

# 1
tuple_d = tuple_a + tuple_b


# 2
tuple_d = (1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9, 10, 11)

res = []
for item in tuple_d:
    count = tuple_d.count(item)
    if count < 2:
        continue
    res.append((item, count))

print(tuple(res))

# 3
tuple_d = (1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9, 10, 11)
res = []
elements = []
for element in tuple_d:
    count = tuple_d.count(element)
    if count < 2 and element in elements:
        continue
    elements.append(element)
    indexes = []
    for index, item in enumerate(tuple_d):
        if item == element:
            indexes.append(index)
    res.append((element, tuple(indexes)))

print(tuple(res))
print(tuple(res) == ((4, (3, 5, 10)), (5, (4, 6, 11)), (6, (7, 12)), (7, (8, 13)), (8, (9, 14))))





list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]

list_d = [[list_a[0], list_b[0]], [list_a[1], list_b[1]],]

tuple_d = (4, 5, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9, 10, 11)

temp_res = ()
# 0, 4
# 2, 4
for index, item in enumerate(tuple_d):
    count = tuple_d.count(item)
#                           0                  0
#                           0                  2
    if count > 1 and tuple_d.index(item) == index:
        test2 = ()
#              0       4
        for index1, item1 in enumerate(tuple_d):
            if item1 == item:
                test2 = test2 + (index1,)
        temp_res = temp_res + ((item, test2),)
print('Tuple_Task #3_1\n', 'res = ', temp_res)


a = 1
a += 1



d = {
    1: {
        2: {
            3: {

            }
        }
    }
}

d.setdefault(1, {}).setdefault(2, {}).setdefault(3, {})



l = list(range(100))

s = 0
for item in l:
    if item % 2 == 0:
        s += item
    s *= 2

a = s


def calc_sum(seq):
    if len(seq) == 0:
        return
    s = 0
    for item in seq:
        if item % 2 == 0:
            s += item
        s *= 2

    return s










l = list(range(300, 4000))

s = 0
for item in l:
    if item % 2 == 0:
        s += item
    s *= 2


def my_func(a, c, b, d):
    if a > b:
        return 1
    return 3


#           =  =  =  =
f = my_func(1, 2, 3, 3)

a = tuple([1, 2, 4, 5])

my_var = 0

my_func(1, 2, 4, 5)


import

a = 1

b = 3


def dfdfs


res = dfdfs(a, b)
dfdfs(res)












