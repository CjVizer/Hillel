import random

k = 7
C = 55

lst = [random.randint(1, 10) for _ in range(10)]
print(lst)
lst.append(0)

for i in range(len(lst) - 1, k, -1):
    lst[i] = lst[i - 1]
lst[k] = C

print(lst)
