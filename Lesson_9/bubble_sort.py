import random


def bubble_sort(my_list):
    cnt = 0
    for i in range(len(my_list)-1):
        cnt += 1
        flag = True
        for j in range(len(my_list)-1-i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                flag = False

        if flag:
            break

    return cnt


lst = [random.randint(10, 99) for _ in range(30)]
print(lst)
res = bubble_sort(lst)
print(res)
print(lst)
