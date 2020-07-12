"""
47. Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão acima da diagonal
principal.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = float(input(f'[[{i}] [{j}]] insira um valor:  '))

print('------------------Matriz-------------\n')

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]}]', end=' ')
    print()

for i in range(0, 3):
    for j in range(0, 3):
        if j > i:
            soma = soma + matriz[i][j]

print(f'A soma: {soma}')