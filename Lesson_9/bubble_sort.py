import random


def bubble_sort(my_list):
    cnt = 0
    for i in range(len(my_list) - 1):
        cnt += 1
        flag = True
        for j in range(len(my_list) - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                flag = False
        if flag:
            break
    return cnt


lst = [random.randint(10, 99) for _ in range(30)]
# lst = [10, 13, 18, 20, 30, 33, 34, 39, 34, 46, 51, 51, 53, 59, 59, 63, 64, 67, 68, 69, 74, 76, 81, 82, 82, 83, 84, 88,
#        90, 95]
print(lst)
res = bubble_sort(lst)
print(res)
print(lst)
