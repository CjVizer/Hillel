symbol_1 = '* '
symbol_2 = '  '

height = int(input('Введите высоту треугольника: '))

for i in range(height):
    for j in range(height * 2 - 1):
        if (i == height - 1
                or j - i == height - 1
                or j + i == height - 1):
            print(symbol_1, end='')
        else:
            print(symbol_2, end='')
    print()

height = int(input('Введите высоту заполненного треугольника: '))

for i in range(height):
    for j in range(height * 2 - 1):
        if j - i <= height - 1 <= j + i:
            print(symbol_1, end='')
        else:
            print(symbol_2, end='')
    print()

height = int(input('Введите высоту ромба №1: '))

for i in range(height):
    for j in range(height):
        if i <= height // 2 and j - i <= height // 2 <= j + i:
            print(symbol_1, end='')
        elif (i - j == height // 2
              or j == height + height // 2 - 1 - i):
            print(symbol_1, end='')
        else:
            print(symbol_2, end='')
    print()

height = int(input('Введите высоту ромба №2: '))

for i in range(height):
    for j in range(height):
        if i <= height // 2 and j - i <= height // 2 <= j + i:
            print(symbol_1, end='')
        elif (i - j == height // 2
              or j == height // 2
              or j == height + height // 2 - 1 - i):
            print(symbol_1, end='')
        else:
            print(symbol_2, end='')
    print()
