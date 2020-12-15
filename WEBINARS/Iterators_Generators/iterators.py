my_list = [1, 2, 3]


class MyNumber:
    def __iter__(self):
        self.value = 1
        return self

    def __next__(self):
        value = self.value
        if value < 1000:
            self.value += 1
            return value
        else:
            raise StopIteration


numbers = MyNumber()
iter_numb = iter(numbers)
for value in iter_numb:
    print(value)

# print(next(iter_numb))
# print(next(iter_numb))
# print(next(iter_numb))
# print(next(iter_numb))
# print(next(iter_numb))
# print(next(iter_numb))


# for value in my_list:
#     print(value)
#
# iter_list = iter(my_list)
# print(iter_list)
#
# print(next(iter_list))
# value = next(iter_list)
# print(value)
# print(next(iter_list))
# print(next(iter_list))
