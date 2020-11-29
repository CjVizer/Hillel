import random


def comp(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def func(lst, comparator):
    for i in range(0, len(lst) - 1, 2):
        el1 = lst[i]
        el2 = lst[i + 1]
        if comparator(el1, el2) > 0:
            print(el1, '>', el2)
        elif comparator(el1, el2) < 0:
            print(el1, '<', el2)
        elif comparator(el1, el2) == 0:
            print(el1, '=', el2)


lst_0 = [random.randint(10, 99) for _ in range(25)]

print(lst_0)
func(lst_0, comp)
