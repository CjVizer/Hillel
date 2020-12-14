"""
Дан словарь ключами которого являются английские слова,
а значения - списки латинских слов. Необходимо развернуть словарь.
Другими словами, необходимо, на основании заданого словаря, создать новый словарь,
у которого в качестве ключей будут взяты латинские слова, из первого словаря,
а значениями будут, соответствующие им, английские слова.

Исходный словарь:

d = {

   'apple': ['malum', 'pomum', 'popula'],

   'fruit': ['baca', 'bacca', 'popum'],

   'punishment': ['malum', 'multa']

}
"""

d = {

    'apple': ['malum', 'pomum', 'popula'],

    'fruit': ['baca', 'bacca', 'popum'],

    'punishment': ['malum', 'multa']

}

k = list(d.keys())
v = list(d.values())
d_my = dict()

for i in range(len(k)):
    for j in range(len(v[i])):
        d_my.update({v[i][j]: d_my.get(v[i][j], []) + [k[i]]})
