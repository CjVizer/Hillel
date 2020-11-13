students_1 = int(input('Сколько учеников в первом математическом классе?: '))
students_2 = int(input('Сколько учеников во втором математическом классе?: '))
students_3 = int(input('Сколько учеников в третьем математическом классе?: '))

desks = students_1 // 2 + students_1 % 2
desks += students_2 // 2 + students_2 % 2
desks += students_3 // 2 + students_3 % 2

print(desks)
