import random

lst = [random.randint(-10, 10) for _ in range(15)]

print(lst)

print('В этом списке', len(set(lst)), 'уникальных чисел.', sorted(set(lst)))
