import random

count = 0
lst = [random.randint(-10, 10) for _ in range(25)]

print(lst)

for i in range(1, len(lst)-1):
    if lst[i-1] < lst[i] > lst[i+1]:
        count += 1

print('Результат: ', count)
