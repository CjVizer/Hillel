t = ()
print(t, type(t))
t = tuple()
t = tuple('Process finished with exit code 0')
print(t)
t = tuple([1, 2, 3, 4, 5, 6])
print(t)
t = (4, 6, 4, 6, 3, 'test', True)
print(t)
print(t[4])

print(t[2: 5])

t = '50', 56
print(t, type(t))

# t[0] = 9
# del t[0]

# len()
print(len(t))

# +
print((1, 2, 3) + (4, 5, 6))

# *
print((1, 2, 3) * 3)

# in
t = (1, 2, 3, 4, 5, 6)
print(4 in t)
print(9 in t)

# for
for element in t:
    print(element)

for idx in range(len(t)):
    print(t[idx])

# index(value, start, stop)
print('index =', t.index(3))

# count()
print(t.count(4))

# sum(), min(), max()

# t = (1, 2, 3)
# r = t + 'rtrwe'
# print(r)