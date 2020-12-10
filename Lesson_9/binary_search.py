from random import randint


def binary_search(array, key_value, left=0, right=None):
    if right is None:
        right = len(array)

    middle = (left + right) // 2
    while array[middle] != key_value and left <= right:
        if array[middle] < key_value:
            left = middle + 1
        else:
            right = middle - 1

        middle = (left + right) // 2

    return (True, middle) if not (left > right) else (False, middle+1)


# Creating a sorted list of random values
lst = []
for i in range(15):
    lst.append(randint(1, 50))
lst.sort()
print(lst)

key = 23
flag, idx = binary_search(lst, key)

print('Flag =', flag)
print('Index =', idx)

# if key value not found, we can insert this value by index
if not flag:
    lst.insert(idx, key)

print(lst)
