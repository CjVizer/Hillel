""""""

"""
while condition:
    operator1
    operator2
    
    operatorN
operatorM
"""

i = 1
while i < 10:
    print(i, end=' ')
    i += 1

print()


# while True:
#     print('X1')

# break
while True:
    num = int(input('Please enter a number:'))
    if num == 0:
        break

    print(num)