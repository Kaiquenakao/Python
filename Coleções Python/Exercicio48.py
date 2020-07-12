"""
48. Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão abaixo da diagonal
principal.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = float(input(f'[[{i}] [{j}]] digite um valor:  '))

print('---------------Matriz--------------')

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]}]', end=' ')
    print()

for i in range(0, 3):
    for j in range(0, 3):
        if i > j:
            soma = matriz[i][j] + soma

print(f'A soma dos números abaixos da diagonal: {soma}')
