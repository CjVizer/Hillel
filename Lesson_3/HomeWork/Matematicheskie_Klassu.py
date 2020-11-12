students_count = int(input('Сколько учеников в первом математическом классе?: '))
students_count += int(input('Сколько учеников во втором математическом классе?: '))
students_count += int(input('Сколько учеников в третьем математическом классе?: '))

print(students_count // 2 + students_count % 2)
