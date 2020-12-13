"""

Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
В качестве параметров, функция получает десятичное число и систему счисления.
Возвращает строку - результат перевода десятичного числа.

Подсказка: в этой задаче вам может понадобиться:

список
метод `revers()` (или срез [::-1],
или вместо `revers()` использовать `insert()` тогда не придётся разворачивать список),
чтоб развернуть список, метод `join()`
строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт `from string import ascii_uppercase`),
она содержит все буквы латинского алфавита.


Алгоритм преобразования десятичного числа в другую систему счисления можно найти в интернете. Например вот здесь.

"""
from string import ascii_uppercase, digits


def conv_notation(f_num, f_notation):
    x = digits + ascii_uppercase
    tmp = []
    while f_num:
        tmp.insert(0, x[f_num % f_notation])
        f_num = f_num // f_notation
    tmp = ''.join(tmp)
    return tmp


num = int(input('Введите число: '))
notation = int(input('В какую систему счисления преобразовать? (2-36): '))

print('Результат: ' + conv_notation(num, notation))
