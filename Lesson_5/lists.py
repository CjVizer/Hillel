a = []
print(a, type(a))
a = list()
a = list('Hello World!')
print(a)
a = [1, 3, 45, 2, 5, -2, 'test', 4.5, True]
print(a)
print(a[3])
print(a[2:5])
print(a[::-1])
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 4)

a = b
print(id(a), id(b))
print(a, b)
a[1] = 20
print(a, b)
a = b.copy()
print(id(a), id(b))
a[1] = 50
print(a, b)

a = a * 3

# len()
print(len(a))
print(a)

# append()

a.append(100)
print(a)

# in

print(6 in a)
print(8 in a)
print(6 not in a)
print(8 not in a)

# min(), max(), sum()
print(min(a))
print(max(a))
print(sum(a))

# index()
print(a.index(6, 3))
# print(a.index(8))

# count()
print(a.count(6))
print(a.count(90))

# pop()
print(a)
print(a.pop())
print(a)

# pop(idx)
print(a.pop(3))
print(a)

# insert(idx, val)
a.insert(3, 80)
print(a)

# clear()
# a.clear()
# print(a)

# del
del a[3]
print(a)

# del a
# print(a)

# extend(list)
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(a)
print(b)
print(c)
a.extend(b)
print(a)
print(b)

# remove()
a.remove(6)
print(a)

# revers()
print(a[::-1])
a.reverse()
print(a)

# join()
# split()

s = 'Process finished with exit code 0'
lst = s.split()
print(lst)

s1 = ' <> '.join(lst)
print(s1)
