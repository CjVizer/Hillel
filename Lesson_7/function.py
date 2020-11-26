"""
def function_name(param1, param2, ... paramN):
    operation1
    operation2
    return value
"""

x = 65


def hello():
    print('Hello World!')


res = hello()
print(res)


def summa(a, b):
    r = a + b
    # print(a + b)
    # return a + b
    return r


res = summa(3, 6)
print(summa(7, res))

# num1 = int(input('Please enter a number1: '))
# num2 = int(input('Please enter a number2: '))
# res = summa(num1, num2)
# print(res)


def print_x():
    global x
    x = 7
    print(x)


print(x)
print_x()
print(x)