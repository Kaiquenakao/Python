"""
51. Leia uma matriz de 3 x 3 elementos. Calcule e imprima a sua transporta
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizt = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = float(input(f'[[{i}] [{j}]] digite um valor:  '))

print('-----------------Matriz------------------')

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]}]', end=' ')
    print()

for i in range(0, 3):
    for j in range(0, 3):
        matrizt[j][i] = matriz[i][j]

print('------------Matriz transporta-------------')

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matrizt[i][j]}]', end=' ')
    print()