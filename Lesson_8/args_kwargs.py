print()
print(1)
print(2, 4, 'erer', True)


def func1(*args):
    print(type(args), args)


func1(2, 4, 'erer', True)


def func2(**kwargs):
    print(type(kwargs), kwargs)


func2(a=4, b='ertyr', c=True, d=3.14)


