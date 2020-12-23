class SomeClass:
    pass


def square_m(self):
    return self.x * 2


def init(self, x):
    self.x = x


print(dir(SomeClass))
SomeClass.new_attr = 35
print(dir(SomeClass))
SomeClass.init = init
print(dir(SomeClass))
SomeClass.square_m = square_m

obj = SomeClass()
print(dir(obj))
obj.init(6)
print(obj.square_m())
