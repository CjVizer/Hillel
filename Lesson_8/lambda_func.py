import random
import pprint

"""
    lambda a, b, c: a + b + c
"""


func = lambda x, y: x + y
print(func(3, 5))

# map, filter, zip
# map(func, collection)

C = [39.2, 36.5, 37.3, 38, 37.8]


# def fahrenheit(temperature):
#     return round(((float(9)/5)*temperature + 32), 2)


# def celsius(temperature):
#     return round((float(5)/9)*(temperature-32), 2)


# lst = []
# for temp in C:
#     lst.append(fahrenheit(temp))
#
# print(lst)

# lst1 = []
# for temp in lst:
#     lst1.append(celsius(temp))
# print(lst1)

res = list(map(lambda temp: round(((float(9)/5)*temp + 32), 2), C))
print(res)

res1 = list(map(lambda temp: round((float(5)/9)*(temp-32), 2), res))
print(res1)


# filter(func, collection)
lst = [random.randint(0, 100) for _ in range(30)]
print(lst)
l = []
for el in lst:
    if el % 2 == 0:
        l.append(el)

print(l)

res = list(filter(lambda x: x == 0, lst))
print(res)

# zip(collection1, collection2, ... )
name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]

name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]

res = dict(zip(name_hero, name_real))
pprint.pprint(res)