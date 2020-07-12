"""
45. Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada posição das
matrizes lida.
"""
matriz1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
contador = 0
matriz3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(0, 4):
    for j in range(0, 4):
        matriz1[i][j] = float(input(f'Matriz [[{i}] [{j}]] digite um valor:  '))

print('---------------Matriz 2------------------')

for i in range(0, 4):
    for j in range(0, 4):
        matriz2[i][j] = float(input(f'Matriz [[{i}] [{j}]] digite um valor:  '))

print('-------------Resultado da Matriz 1---------------')

for i in range(0, 4):
    for j in range(0, 4):
        print(f'[{matriz1[i][j]}]', end=' ')
    print()

print('-------------Resultado da Matriz 2---------------')

for i in range(0, 4):
    for j in range(0, 4):
        print(f'[{matriz2[i][j]}]', end=' ')
    print()

print('------------------Resultado Final--------------------')

for i in range(0, 4):
    for j in range(0, 4):
        if matriz1[i][j] > matriz2[i][j]:
            matriz3[i][j] = matriz1[i][j]
        else:
            matriz3[i][j] = matriz2[i][j]

for i in range(0, 4):
    for j in range(0, 4):
        print(f'[{matriz3[i][j]}]', end=' ')
    print()
