"""
62. Faça um programa que leia uma matriz A de tamanho 3 x 3 e calcule B = A²
"""
A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print('=========== Matriz A ===========\n')
for i in range(0, 3):
    for j in range(0, 3):
        A[i][j] = float(input(f'Linha: [{i}] Coluna: [{j}] Insira um valor:  '))

for i in range(0, 3):
    for j in range(0, 3):
        B[i][j] = A[i][j] * A[i][j]

print('============== A ===============\n')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{A[i][j]}]', end=' ')
    print()

print('============== B ===============\n')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{B[i][j]}]', end=' ')
    print()



