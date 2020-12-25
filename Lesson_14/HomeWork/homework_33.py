"""
Создать класс, описывающий группу студентов - `Group`.
Данный класс хранит студентов в виде списка объектов `Student`
также реализованного в виде соответствующего класса.

В классах реализовать необходимай набор атрибутов
(Например класс `Student` должен иметь атрибуты `name`, `age`, `grades`),
а так же необходимый набор методов экземпляра для работы с этими экземплярами.
"""


class Student:
    def __init__(self, name, age=None, mail=None, phone=None):
        self.__name = name
        self.__age = age
        self.__mail = mail
        self.__phone = phone
        self.__grades = []

    def get_student(self):
        return [self.__name, self.__age, self.__mail, self.__phone, self.__grades]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self, mail):
        self.__mail = mail

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grade):
        self.__grades.append(grade)

    def clear_grades(self):
        self.grades.clear()


class Group:
    def __init__(self):
        self.students = []
        self.debug = False
        self.__warn_empty_group = 'В этой группе пока нет студентов :('
        self.__warn_no_such_student = 'Студента с индексом {} в этой группе нет :('

    def get_group(self):
        if len(self.students):
            return [student.get_student() for student in self.students]
        elif self.debug:
            print('get_group() ' + self.__warn_empty_group)

    def get_student(self, idx):
        if idx < len(self.students):
            return self.students[idx].get_student()
        elif self.debug:
            print('get_student() ' + self.__warn_no_such_student.format(idx))

    def add_student(self, name, age=None, mail=None, phone=None, grades=None):
        self.students.append(Student(name, age, mail, phone))
        if grades and isinstance(grades, list):
            for i in range(len(grades)):
                self.students[len(self.students) - 1].grades = grades[i]
        elif grades:
            self.students[len(self.students) - 1].grades = grades

    def get_name(self, idx):
        if idx < len(self.students):
            return self.students[idx].name
        elif self.debug:
            print('get_name() ' + self.__warn_no_such_student.format(idx))

    def set_name(self, idx, name):
        if idx < len(self.students):
            self.students[idx].name = name
        elif self.debug:
            print('set_name() ' + self.__warn_no_such_student.format(idx))

    def get_age(self, idx):
        if idx < len(self.students):
            return self.students[idx].age
        elif self.debug:
            print('get_age() ' + self.__warn_no_such_student.format(idx))

    def set_age(self, idx, age):
        if idx < len(self.students):
            self.students[idx].age = age
        elif self.debug:
            print('set_age() ' + self.__warn_no_such_student.format(idx))

    def get_mail(self, idx):
        if idx < len(self.students):
            return self.students[idx].mail
        elif self.debug:
            print('get_mail() ' + self.__warn_no_such_student.format(idx))

    def set_mail(self, idx, mail):
        if idx < len(self.students):
            self.students[idx].mail = mail
        elif self.debug:
            print('set_mail() ' + self.__warn_no_such_student.format(idx))

    def get_phone(self, idx):
        if idx < len(self.students):
            return self.students[idx].phone
        elif self.debug:
            print('get_phone() ' + self.__warn_no_such_student.format(idx))

    def set_phone(self, idx, phone):
        if idx < len(self.students):
            self.students[idx].phone = phone
        elif self.debug:
            print('set_phone() ' + self.__warn_no_such_student.format(idx))

    def get_grades(self, idx):
        if idx < len(self.students):
            return self.students[idx].grades
        elif self.debug:
            print('get_grades() ' + self.__warn_no_such_student.format(idx))

    def add_grades(self, idx, grades):
        if idx < len(self.students):
            if grades and isinstance(grades, list):
                for i in range(len(grades)):
                    self.students[idx].grades = grades[i]
            elif grades:
                self.students[idx].grades = grades
        elif self.debug:
            print('add_grades() ' + self.__warn_no_such_student.format(idx))

    def delete_student(self, idx):
        if idx < len(self.students):
            self.students.pop(idx)
        elif self.debug:
            print('delete_student() ' + self.__warn_no_such_student.format(idx))
