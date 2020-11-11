""""""

"""
if condition:
    operator1
    operator2
    
    operatorN
    
operatorM
"""

a = 16
if a < 10:
    print('True')

"""
if condition:
    operator1
    operator2
else:
    operator3
    operator4   
"""

a = 16
if a < 10:
    print('True')
else:
    print('False')

"""
if condition1:
    operator1
else:
    if condition2:
        operator2
    else:
        if condition3:
            operator3
        else:
            operator4 
"""
"""
if condition1:
    operator1
elif condition2:
    operator2
elif condition3:
    operator3
else:
    operator4   
"""

# a > 10 and a < 20
# 10 < a < 20

a = 6
if a < 10:
    print('a < 10')
elif 10 < a < 20:
    print('a > 10 and a < 20')
else:
    print('a > 20')

# res = A ? B : C
"""
if A:
    res = B
else:
    res = C
"""

a = 4
b = 7
c = 3

res = b if a < 10 else c

if a < 10:
    res = b
else:
    res = c
