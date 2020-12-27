# def func():
#     x = 3
#     x += 1
#
#     def inner():
#         print(x, id(x))
#         # x += 1
#
#     return inner
#
#
# r = func()
# print(r)
# r()
# r()
# r()
# r()

def measure_time(func):
    from datetime import datetime

    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        print(datetime.now() - start)
        return res

    return wrapper


@measure_time
def gen1(cnt):
    lst = []
    for i in range(cnt):
        if i % 2 == 0:
            lst.append(i)
    return lst


@measure_time
def gen2(cnt):
    lst = [i for i in range(cnt) if i % 2 == 0]
    return lst


print(len(gen1(10**6)))
print(len(gen2(10**6)))
