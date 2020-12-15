# import sys


def reader_wrapper(g):
    yield from g


lst = [1, 5, 8, 10, 12]

func = reader_wrapper(lst)

print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
# print(next(reader_wrapper([1, 2, 3])))

# size = 3
#
#
# def create_generator(size):
#     print("START")
#     for number in range(size):
#         print("***")
#         yield number ** 2
#
#
# my_object = create_generator(size)
# print(my_object[1])
# print(my_object, type(my_object))
# print(my_object)
# print("-----------------")
# print(next(my_object))
# print(next(my_object))
# for numb in my_object:
#     print(">>>", numb)

# my_list = [number ** 2 for number in range(size)]
# print('Size of my_list: ', sys.getsizeof(my_list))

# for value in my_list:
#     print(value)

# my_generator = (number ** 2 for number in range(size))
# print(my_generator)
# print('Size of my_generator: ', sys.getsizeof(my_generator))

# print(next(my_generator))
# print(next(my_generator))
#
# print(next(my_generator))
# print(next(my_generator))
# for value in my_generator:
#     print(value)
