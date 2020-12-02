import random


def quick_sort(array, first_idx, last_idx):
    if first_idx >= last_idx:
        return

    i, j = first_idx, last_idx
    middle_value = array[(first_idx + last_idx) // 2]
    while i <= j:
        while array[i] < middle_value:
            i += 1

        while array[j] > middle_value:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i+1, j-1

    quick_sort(array, first_idx, j)
    quick_sort(array, i, last_idx)


lst = [random.randint(10, 99) for _ in range(30)]
print(lst)

quick_sort(lst, 0, len(lst)-1)
print(lst)
