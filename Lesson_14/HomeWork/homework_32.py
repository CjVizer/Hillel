"""
Реализовать класс цифрового счетчика.
Обеспечьте возможность установки максимального и минимального значений,
увеличения счетчика на 1,
возвращения текущего значения.
"""


class Counter:
    def __init__(self, min_value=0, max_value=100):
        self.__min_value = min_value
        self.__max_value = max_value
        self.__value = min_value

    def counter_update(self):
        self.__value = (self.__value + 1) if self.__value < self.__max_value else self.__min_value

    def get_value(self):
        return self.__value
