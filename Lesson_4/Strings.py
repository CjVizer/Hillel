print(chr(0x26bd))
print('\u26bd')
print(chr(9917))

print(ord('⚽'))
print(hex(ord('⚽')))

wave = '~'
boat = '\U0001F6A3'
seagull = '\u033C'
fish = '\U0001F41F'
penguin = '\U0001F427'
wale = '\U0001F40B'
octopus = '\U0001F419'

row = wave * 10 + boat + wave * 15 + '\n'
fish_row = wave * 4 + fish + wave * 21 + '\n'
wale_row = wave * 10 + wale + wave * 15 + '\n'
penguin_row = wave * 7 + penguin + wave * 18 + '\n'
octopus_row = wave * 17 + octopus + wave * 8 + '\n'

sea = row + fish_row + wale_row + penguin_row + octopus_row
print(sea)


s = 'Process finished with exit code 0'
print(s)

# len(s)
print(len(s))

print(s[0])
print(s[-1])

# str[start: stop: step]
print(s[8: 16: 2])
print(s[4])
print(s[-5])
print(s[1:])
print(s[: 8])
# print(s[50])
print(s[5: 3874562437896547893653497865])
print(s[-23874564735478:])
print(s[::-1])

for symbol in s:
    print(symbol, end='')
print()

for idx in range(len(s)):
    print(s[idx], end=' ')
print()

# find(substring, start, end)
idx = s.find('it')
print(idx)
idx = s.find('it', idx + len('it'))
print(idx)
idx = s.find('it', idx + len('it'))
print(idx)

# rfind(substring, start, end)

# replace(old, new, count)
s1 = s.replace('it', 'IT', 1)
print(s1)

# count(substring, start, end)
print(s.count('i'))

# capitalize()
s = 'proCess fINishEd with exit code 0'
print(s.capitalize())

# title()
print(s.title())

# upper()
# lower()
print(s.upper())
print(s.lower())

s = '         proCess fINishEd with exit code 0                 '
# strip(substring)
print('"' + s + '"')
print('"' + s.strip() + '"')
