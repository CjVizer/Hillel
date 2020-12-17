with open('src_14.txt', encoding='utf-8') as src:
    buffer = src.read()

buffer = [line.split() for line in buffer.strip('\n').split('\n')]

for line_idx in range(len(buffer)):
    cnt = len(buffer[line_idx]) - 2
    for value in buffer[line_idx][3:]:
        buffer[line_idx][2] = str(int(buffer[line_idx][2]) + int(buffer[line_idx].pop(-1)))
    buffer[line_idx][2] = str(round(float(buffer[line_idx][2]) / cnt, 2))

for line in buffer:
    if float(line[-1]) < 5:
        print('{name_surname:<25}{average}'.format(name_surname=' '.join(line[:2]), average=line[-1]))
print()
print('Cредний балл по классу: ', round(sum(map(float, [buffer[i][-1] for i in range(len(buffer))])) / len(buffer), 2))

buffer2 = ''
for line_id in range(len(buffer)):
    buffer2 += '{name_surname:<20}{average}\n'.format(
        name_surname=' '.join([buffer[line_id][1], buffer[line_id][0][0] + '.']),
        average=buffer[line_id][-1])

with open('dst_14.txt', 'w', encoding='utf-8') as dst:
    dst.write(buffer2)
