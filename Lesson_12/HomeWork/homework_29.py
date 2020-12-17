from random import randint

M = int(input('Введите кол-во строк: '))
N = int(input('Введите кол-во колонок: '))

print()

matrix = [[randint(10, 50) for _ in range(N)] for _ in range(M)]
matrix.append([0] * N)

for line_idx in range(M):
    matrix[line_idx].append(0)
    for value_idx in range(N):
        matrix[line_idx][-1] += matrix[line_idx][value_idx]
        matrix[-1][value_idx] += matrix[line_idx][value_idx]

for line_idx in range(M):
    print(''.join('{i:>4}'.format(i=matrix[line_idx][symb_idx]) for symb_idx in range(N)) +
          '{summa:>10}'.format(summa=matrix[line_idx][-1]))
print()
print(''.join('{i:>4}'.format(i=matrix[-1][symb_idx]) for symb_idx in range(N)))
