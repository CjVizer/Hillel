s = {}
print(s, type(s))

s = {1, 2, 3, 4}
print(s, type(s))
s = set()
print(s, type(s))
s = set('Process finished with exit code 0')
print(s)

a = {1, 2, 3}
b = {3, 2, 3, 1}
print(a == b)
print(a, b)

for value in b:
    print(value)

a = {2, 6, 4, 5, 7, 8, 9}
b = {0, 5, 3, 2, 1, 7, 6}

# A | B         A.union(B)
# A |= B        A.update(B)
print(a | b)
# a |= b      # a = a | b
# print(a)

# A & B         A.intersection(B)
# A &= B        A.intersection_update(B)
print(a & b)

# A - B         A.difference(B)
# A -= B        A.difference_update(B)
print(a - b)

# A ^ B         A.symmetric(B)
# A ^= B        A.symmetric_update(B)
print(a ^ b)
x = a - b
y = b - a
print(x | y)

fs = frozenset(a)
print(fs)