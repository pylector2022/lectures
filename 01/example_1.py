raw_a = input('Please input a: ')
raw_b = input('Please input b: ')

size_a = int(raw_a)
size_b = int(raw_b)

perimeter = (size_a + size_b) * 2

"""
20
if perimeter > 20 then print(...) else print(...)
"""
if perimeter > 20:
    print(perimeter / 2)
else:
    print(perimeter / 4)

# if perimeter > 20:
#     print(perimeter / 2)
# elif perimeter == 20:
#     print(perimeter)
# elif perimeter == 20:
#     print(perimeter)
# else:
#     print(perimeter / 4)


