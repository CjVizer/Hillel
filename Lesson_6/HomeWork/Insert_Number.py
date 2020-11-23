import random

k = -2
C = 55

lst = [random.randint(1, 10) for _ in range(20)]
print(lst)
# lst.append(0)
# print(lst)

# for i in range(len(lst)-1, k, -1):
#     lst[i] = lst[i-1]
# lst[k] = C
lst.insert(-1, 33)
print(lst)
