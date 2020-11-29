"""

Дан текст состоящий из нескольких строки.
Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите последнее.

Задачу необходимо решить с использованием словаря.

"""

res = {}
counter = 0
result = ''

while True:
    words = input('Введите текст, для выхода из цикла введите "exit": ').split(' ')
    if words[0] == 'exit':
        break

    for word in words:
        res[word] = res.get(word, 0) + 1
        if res[word] >= counter:
            counter = res.get(word, 0)
            result = word

print('Ответ:', result)
