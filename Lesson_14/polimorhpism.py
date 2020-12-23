class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # def __set_name(self, name):
    #     self.__name = name
    #
    # def __get_name(self):
    #     return self.__name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def set_age(self, age):
        if 0 < age < 100:
            self.__age = age

    def display(self):
        print('Имя:', self.__name, '\tВозраст:', self.__age)

    # __name = property(__get_name, __set_name)


class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.__company = company

    def display(self):
        super().display()
        print('Компания:', self.__company)


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.__university = university

    def display(self):
        print('Студент:', self.__name, 'учится в универе:', self.__university)


# people = [Person('Tom', 23), Employee('Bob', 35, 'Google'), Student('Sam', 19, 'Harvard')]
#
# for person in people:
#     person.display()

person = Person('Tom', 23)
person.display()

person.name = 'Tim'
print(person.name)



