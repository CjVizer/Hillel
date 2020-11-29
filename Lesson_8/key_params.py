def pow(a=3, b=2):
    print('a =', a, 'b =', b)
    return a ** b


res = pow(4, 5)
print(res)

res = pow(4, 2)
print(res)

res = pow(4)
print(res)

res = pow()
print(res)


def func(a, b, c, d=1, e=2, f=3):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e, 'f =', f)


func(10, 20, 30)
func(10, 20, 30, 40)
func(10, 20, 30, 40, 50)
func(10, 20, 30, 40, 50, 60)

func(10, 20, 30, f=60, e=100)
func(f=50, a=80, e=30, b=20, c=90)


def func1(a, b=None):
    print('a =', a, 'b =', b, end='\t')
    if b is None:
        b = []

    b.append(a)
    print('a =', a, 'b =', b)


lst = []
func1(4, lst)

func1(1)
func1(2)
func1(3)
