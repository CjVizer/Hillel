"""
class ClassName(parentClass1, parentClass2, ... parentClassN):
    body of class
"""


class Human:
    sex = 'Man'
    age = 26
    height = 183
    phone = '(372) 457-236-123-57'


h = Human()
# print(type(h))
# print(h.age)


class Child(Human):
    age = 18


ch = Child()
# print(ch.height)
# print(ch.age)


class Point:
    # x = 0
    # y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


pt1 = Point()
print(pt1.x, pt1.y)
pt2 = Point(3, 6)
print(pt2.x, pt2.y)
pt3 = Point(5)
print(pt3.x, pt3.y)

pt1.x = 9
print(pt1.x)
