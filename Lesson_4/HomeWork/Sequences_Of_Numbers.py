symbol_count = 0
symbol_sum = 0
symbol_average = 0
symbol_min = 0
symbol_max = 0
symbol_even_count = 0
symbol_odd_count = 0

while True:
    N = int(input('Введите число: '))
    if N == 0:
        break
    symbol_count += 1
    symbol_sum += N
    symbol_average = symbol_sum / symbol_count
    if symbol_min == 0:
        symbol_min = N
    elif N < symbol_min:
        symbol_min = N
    if symbol_max == 0:
        symbol_max = N
    elif N > symbol_max:
        symbol_max = N
    if N % 2 == 0:
        symbol_even_count += 1
    else:
        symbol_odd_count += 1

print('Количество введённых чисел:', symbol_count)
print('Сумма введённых чисел:', symbol_sum)
print('Среднее арифметическое всех введённых чисел:', symbol_average)
print('Минимальное значение:', symbol_min)
print('Максимальное значение:', symbol_max)
print('Количество чётных чисел:', symbol_even_count)
print('Количество нечётных чисел:', symbol_odd_count)
