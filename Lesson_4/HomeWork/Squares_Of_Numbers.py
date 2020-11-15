N = int(input('Введите натуральное число: '))

print(N, ' ', end='')
i = 1

while i**2 <= N:
    print(i**2, '', end='')
    i += 1
