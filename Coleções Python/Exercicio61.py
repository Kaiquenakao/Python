"""
61. Faça um programa que leia duas matrizes A e B de tamanho 3 x 3 e calcule C = A * B.
"""
A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print('=========== Matriz A ===========')
for i in range(0, 3):
    for j in range(0, 3):
        A[i][j] = float(input(f'Linha: [{i}] Coluna: [{j}] Insira um valor:  '))

print('=========== Matriz B ============')
for i in range(0, 3):
    for j in range(0, 3):
        B[i][j] = float(input(f'Linha: [{i}] Coluna: [{j}] Insira um valor:  '))


print('========== A ==============\n')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{A[i][j]}]', end=' ')
    print()

print('========== B ==============\n')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{B[i][j]}]', end=' ')
    print()

print('============ Matriz C ===========')
for i in range(0, 3):
    for j in range(0, 3):
        C[i][j] = A[i][j] * B[i][j]
        print(f'[{C[i][j]}]', end=' ')
    print()

