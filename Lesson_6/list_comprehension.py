import random

lst1 = []
for _ in range(20):
    lst1.append(random.randint(10, 50))

print(lst1)


lst2 = [random.randint(10, 50) for _ in range(20)]
print(lst2)

"""
                1     |         2           |   3
variable = [expression for _ in iterable_obj filter]
"""


lst1 = [25, 11, 29, 23, 25, 46, 50, 30, 27, 17, 33, 22, 48, 49, 22, 13, 14, 18, 24, 44]
lst2 = [25, 11, 29, 23, 25, 46, 50, 30, 27, 17, 33, 22, 48, 49, 22, 13, 14, 18, 24, 44]


lst3 = []
for value in lst1:
    if value % 2 == 0:
        lst3.append(value)

print(lst3)

lst4 = [value for value in [random.randint(10, 50) for _ in range(20)] if value % 2 == 0]
print(lst4)


s = 'Process finished with exit code 0'

s1 = ''.join([a.upper() for a in s])
print(s1)

# enumerate()
for idx, value in enumerate(s):
    print(idx, value)

s2 = ''.join([value.upper() if num % 2 == 0 else value.lower() for num, value in enumerate(s)])
print(s2)