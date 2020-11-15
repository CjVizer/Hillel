s = input('Введите строку: ')
first_entry = s.find('h')
last_entry = s.rfind('h')

print(s[:first_entry+1]+s[first_entry+1:last_entry].replace('h', 'H')+s[last_entry:])
