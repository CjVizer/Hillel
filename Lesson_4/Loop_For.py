""""""

"""
for <variable> in <iterable object>:
    operator1
    operator2
"""

i = 1
for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
    print('#', i, ' color of rainbow is ', color, sep='')
    i += 1


# range(start=0, stop, step=1)
for i in range(1, 100, 2):
    print(i, end=' ')
print()

for i in range(50):
    print(i, end=' ')
print()

"""
for _ in <iterable object>:
    operator1
    operator2    
"""

n = 1
for _ in range(10):
    print(n)
    n += 1
