"""

Написать функцию, принимающую ТРИ параметра
и выполняющая циклически сдвиг целого числа (первый параметр) на N разрядов (второй параметр) вправо или влево,
в зависимости от значения третьего параметра функции.

Третий параметр булевский, задаёт направление сдвига (по умолчанию влево (False)).

Функция должна возвращать ЦЕЛОЕ ЧИСЛО!

"""


def number_shift(num, shift, direction=False):
    num = [i for i in str(num)]
    if direction:
        for _ in range(shift):
            num.insert(0, num.pop())
    else:
        for _ in range(shift):
            num.append(num.pop(0))
    return int(''.join(list(num)))
