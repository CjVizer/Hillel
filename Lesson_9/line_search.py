import random

lst = [random.randint(10, 99) for _ in range(30)]
print(lst)

key = int(input('Please enter a value: '))

for idx in range(len(lst)):
    if lst[idx] == key:
        print('idx =', idx)
        break
