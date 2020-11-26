from pprint import pprint

d = {}
print(d, type(d))
d = dict()
print(d, type(d))

d = {
    0: 'zero',
    1: 'one',
    2: 'two',
}
print(d, type(d))

d = dict(
    [
        (0, 'zero'),
        (1, 'one'),
        (2, 'two')
    ]
)
print(d, type(d))

d = dict(
    zero=0,
    one=1,
    two=2
)
print(d, type(d))

d = {}
print(d, type(d))
d[0] = 'zero'
d[1] = 'one'
d[0] = 'abcd'
print(d, type(d))
# d[-1]

person = {}
person['name'] = 'Ivan'
person['surname'] = 'Ivanov'
person['age'] = 35
person['phone'] = '+38023543645523'
person['children'] = ['Sergey', 'Olga', 'Viktor']
person['pets'] = {'dogs': ['Fido', 'Pluto'], 'cats': ['Fox']}

pprint(person)
print(person['name'])
print(person['children'][1])
print(person['pets']['dogs'][0])
person['pets']['cats'].append('Murzik')
pprint(person)

# in
print('name' in person)

# len()
print(len(person))

# clear()
# pprint(person)
# person.clear()
# pprint(person)

# print(person['name'])
# get(key, default_value)
print(person.get('name', 'Default'))

# keys()
print(list(person.keys()))

# values()
print(list(person.values()))

# items()
pprint(list(person.items()))
for key, value in person.items():
    print(key, value)

# pop()
age = person.pop('age')
print(age)
pprint(person)

# popitem()
res = person.popitem()
print(res)
pprint(person)

# update(dict)
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 100, 'b': 200, 'e': 300}
d1.update(d2)
print(d1)

# fromkeys()
d = dict.fromkeys([1, 2, 3, 4, 5])
print(d)