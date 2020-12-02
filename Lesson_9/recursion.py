def pow_iter(num, ex):
    res = 1
    while ex > 0:
        res *= num
        ex -= 1

    return res


def pow_rec(num, ex):
    if ex == 0:
        return 1

    return num * pow_rec(num, ex - 1)


print(pow_iter(2, 4))
print(pow_rec(2, 4))


def fact_iter(num):
    res = 1
    for i in range(1, num + 1):
        res *= i

    return res


def fact_rec(num):
    if num == 1:
        return 1

    return num * fact_rec(num - 1)


print(fact_iter(5))
print(fact_rec(5))


def fib_iter(num):
    n1 = 0
    n2 = 1
    while num > 1:
        res = n1 + n2
        n1 = n2
        n2 = res
        num -= 1

    return n2


def fib_rec(num):
    # if num == 0 or num == 1:
    #     return num

    return num if num == 0 or num == 1 else fib_rec(num - 1) + fib_rec(num - 2)


print(fib_iter(14))
print(fib_rec(14))
