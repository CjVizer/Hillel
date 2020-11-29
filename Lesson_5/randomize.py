import random

"""
    randint(start, end)
    randrange(start, end, step)
    random()
    uniform(start, end)
"""

# randrange
for _ in range(15):
    print(random.randrange(1, 10, 2), end=', ')
print()

# randint
for _ in range(15):
    print(random.randint(1, 10), end=', ')
print()

# random
for _ in range(15):
    print(random.random(), end=', ')
print()

# uniform
for _ in range(15):
    print(random.uniform(0.1, 9.9), end=', ')
print()