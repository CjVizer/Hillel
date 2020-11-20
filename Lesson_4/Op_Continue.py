# i = 0
# while i < 100:
#     i += 1
#     if i % 3 == 0:
#         continue
#
#     print(i)


num = int(input('Please enter a number: '))
while num != 0:
    if num < 0:
        break
    print('Your number:', num)
    num = int(input('Please enter a number: '))
else:
    print('No negative value.')
