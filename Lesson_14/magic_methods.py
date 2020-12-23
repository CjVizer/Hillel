class Point:
    s = 'Attribute of Class'

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return 'x = {}\ty= {}'.format(self.x, self.y)


pt1 = Point(3, 5)
pt2 = Point(8, 2)

# new_x = x1 + x2, new_y = y1 + y2
pt3 = pt1 + pt2
print(pt3)
