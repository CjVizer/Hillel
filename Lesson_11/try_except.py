# while True:
#     try:
#         a = int(input('Please enter a first number: '))
#         if a == 0:
#             break
#         b = int(input('Please enter a second number: '))
#         print(a / b)
#
#     except ZeroDivisionError:
#         print('Попытка деления на 0')
#     except ValueError:
#         print('Неверные входные данные')
#     else:
#         print('Ошибок нет.')

# finally

try:
    file = open('test.txt', 'w')
    file.write('Some text')
except Exception as ex:
    print('error', ex)
finally:
    print('Finally')
    if not file:
        file.close()
