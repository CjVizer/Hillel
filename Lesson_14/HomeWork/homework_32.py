"""
Реализовать класс цифрового счетчика.
Обеспечьте возможность установки максимального и минимального значений,
увеличения счетчика на 1,
возвращения текущего значения.
"""


class Counter:
    def __init__(self, min_value=0, max_value=100):
        self.min_value = min_value
        self.max_value = max_value
        self.value = min_value

    def counter_update(self):
        self.value = (self.value + 1) if self.value < self.max_value else self.min_value

    def get_value(self):
        return self.value
