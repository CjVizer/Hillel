# import mod1 as m1
# from random import randint, uniform
# from mod1 import func as f1
# from mod2 import func as f2

# from mod1 import *


# lst = ['A', 'B', 'C', 'D', 7, 9, 0]
# mod1.func(lst)

print(dir())


# print(mod1.string)

# f1([1, 2, 3, 4])
# f2([6, 7, 8, 9])
#
# print(m1.pi)

def f():
    from random import randint
    lst = [randint(1, 100) for _ in range(10)]
    return lst


print(f())
