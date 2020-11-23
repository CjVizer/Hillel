import random

a = [random.randint(0, 100) for _ in range(10)]
b = [random.randint(0, 100) for _ in range(10)]

print(a)
print(b)

print('Result:', len(set(a).union(set(b))))
