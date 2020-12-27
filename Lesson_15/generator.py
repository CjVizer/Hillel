def gen_1(num):
    res = []
    while num != 0:
        res.append(num - 1)
        num -= 1
    return res


print(gen_1(10))

for i in gen_1(10):
    print(i, end=', ')
print()

for i in range(10):
    print(i, end=', ')
print()


# yield

def gen_2(num):
    while num != 0:
        yield num - 1
        num -= 1


for i in gen_2(10):
    print(i, end=', ')
print()

print(range(10))
print(gen_2(10))

it = gen_2(10)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))
