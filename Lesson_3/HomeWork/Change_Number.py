number = int(input('Введите целое, положительное, трёхзначное число: '))

print(number % 10 * 100 + number // 10 % 10 * 10 + number // 100)
