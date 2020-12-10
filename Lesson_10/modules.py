from Lesson_10.modules_m import mod1
from Lesson_10.modules_m import mod2
from Lesson_10.modules_m import mod3

# import mod1 as m1
# import mod2
# from random import randint, uniform
#
# from mod1 import func as f1
# from mod2 import func as f2

# from lesson_10.mod1 import *
# from lesson_10.mod2 import *

lst = ['A', 'B', 'C', 'D', 7, 9, 0]
mod1.func(lst)

print(dir())


# print(mod1.string)
# print(randint(1, 10))
# mod1.func(lst)
# mod2.func(lst)

# func([1, 2, 3])
# f1([1, 2, 3, 4])
# f2([6, 7, 8, 9])
# print(m1.string)

# print(string)
# func([1, 2, 3, 4])


def f():
    from random import randint
    lst = [randint(1, 100) for _ in range(10)]
    return lst


print(f())
