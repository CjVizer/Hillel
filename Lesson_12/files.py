"""
    r       read        (default)
    w       write
    x       exclusive
    a       append

    t       text        (default)
    b       binary

    +       mix
"""

lst = [
    'r       read        (default)',
    'w       write',
    'x       exclusive',
    'a       append',
    't       text        (default)',
    'b       binary',
    '+       mix'
]

file = open('example_file.txt', 'w', encoding='utf-8')
for line in lst:
    file.write(line)
    file.write('\n')
file.close()

