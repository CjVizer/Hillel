"""
Создать класс, описывающий группу студентов - `Group`.
Данный класс хранит студентов в виде списка объектов `Student`
также реализованного в виде соответствующего класса.

В классах реализовать необходимай набор атрибутов
(Например класс `Student` должен иметь атрибуты `name`, `age`, `grades`),
а так же необходимый набор методов экземпляра для работы с этими экземплярами.
"""


class Student:
    def __init__(self, name=None, age=None, course=None, grades=None):
        self.name = name
        self.age = age
        self.course = course
        self.grades = [] + grades

    def get_student(self):
        return [self.name, self.age, self.course, self.grades]

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_course(self, course):
        self.course = course

    def get_course(self):
        return self.course

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_grades(self):
        return self.grades

    def clear_grades(self):
        self.grades.clear()


class Group:
    def __init__(self):
        self.students = []

    def get_group(self):
        return [student.get_student() for student in self.students] if len(self.students) else None

    def add_student(self, name=None, age=None, course=None, grades=None):
        self.students.append(Student(name, age, course, grades))

    def get_student(self, idx):
        return self.students[idx].get_student() if idx < len(self.students) else None

    def get_name(self, idx):
        return self.students[idx].get_name() if idx < len(self.students) else None

    def set_name(self, idx, name):
        self.students[idx].set_name(name) if idx < len(self.students) else None

    def get_age(self, idx):
        return self.students[idx].get_age() if idx < len(self.students) else None

    def set_age(self, idx, age):
        self.students[idx].set_age(age) if idx < len(self.students) else None

    def get_course(self, idx):
        return self.students[idx].get_course() if idx < len(self.students) else None

    def set_course(self, idx, course):
        self.students[idx].set_course(course) if idx < len(self.students) else None

    def get_grades(self, idx):
        return self.students[idx].get_grades() if idx < len(self.students) else None

    def add_grade(self, idx, grade):
        self.students[idx].set_grades(grade) if idx < len(self.students) else None

    def delete_student(self, idx):
        if idx < len(self.students):
            self.students.pop(idx)


g = Group()
# g.add_student('Vika', 20, 2, [1, 2, 3, 4, 5])
# g.add_student('Misha', 32, 4, [1, 2, 3, 4, 5])
# g.add_student('Egor', 27, 1, [10, 2, 7, 4, 9])
print(g.get_group())
g.set_name(1, 'Olya')
print(g.get_group())
g.set_age(2, 152)
print(g.get_group())
g.set_course(0, 999)
print(g.get_group())
