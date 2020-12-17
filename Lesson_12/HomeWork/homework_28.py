from random import randint


def my_print(mtx):
    for line_idx in range(M):
        print(''.join('{i:>4}'.format(i=value) for value in matrix[line_idx]))
    print(''.join('{i:>4}'.format(i=value) for value in summa))


def matrix_sort(mtx):
    for i in range(M - 1):
        for j in range(M - 1 - i):
            if summa[j] > summa[j + 1]:
                summa[j], summa[j + 1] = summa[j + 1], summa[j]
                for o in range(M):
                    mtx[o][j], mtx[o][j + 1] = mtx[o][j + 1], mtx[o][j]

    for i in range(M):
        for j in range(M - 1):
            for k in range(M - 1 - j):
                if i % 2 == 0 and mtx[k][i] < mtx[k + 1][i]:
                    mtx[k][i], mtx[k + 1][i] = mtx[k + 1][i], mtx[k][i]
                if i % 2 and mtx[k][i] > mtx[k + 1][i]:
                    mtx[k][i], mtx[k + 1][i] = mtx[k + 1][i], mtx[k][i]

    return mtx


M = int(input('Введите размер матрицы: '))

matrix = [[randint(1, 50) for _ in range(M)] for _ in range(M)]
summa = [sum([matrix[line_idx][value_idx] for line_idx in range(M)]) for value_idx in range(M)]

print()
print('До сортировки')
my_print(matrix)
print()
print('После сортировки')
my_print(matrix_sort(matrix))
