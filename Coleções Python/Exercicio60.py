"""
60. Faça um programa que leia duas matrizes 2 x 2 com valores reais. Ofereça ao usuário um menu
de opções:

(a) somar as duas matrizes
(b) subtrair a primeira matriz da segunda
(c) adicionar uma constante às duas matrizes
(d) imprimir as matrizes

Nas duas primeiras opções uma terceira matriz 3 x 3 deve ser criada. Na terceira opção o valor da
constante deve ser lido e o resultado da adição da constante deve ser armazenada na própria matriz
"""
matriz1 = [[0, 0], [0, 0]]
matriz2 = [[0, 0], [0, 0]]
matrizsoma = [[0, 0], [0, 0]]
matrizsub = [[0, 0], [0, 0]]
matrizconst = [[0, 0], [0, 0]]

print('======== Matriz 1 ========\n')

for i in range(0, 2):
    for j in range(0, 2):
        matriz1[i][j] = float(input(f'Linha: {i} - Coluna: {j} Insira um número:  '))

print('======= Matriz 2 ========\n')

for i in range(0, 2):
    for j in range(0, 2):
        matriz2[i][j] = float(input(f'Linha: {i} - Coluna: {j} Insira um número:  '))

# Soma
for i in range(0, 2):
    for j in range(0, 2):
        matrizsoma[i][j] = matriz1[i][j] + matriz2[i][j]

# Subtração
for i in range(0, 2):
    for j in range(0, 2):
        matrizsub[i][j] = matriz1[i][j] - matriz2[i][j]

# Constante
for i in range(0, 2):
    for j in range(0, 2):
        matrizconst[i][j] = input(f'Linha: {i} - Coluna: {j} Insira um número:  ')

print('============ MATRIZ 1 ============')

for i in range(0, 2):
    for j in range(0, 2):
        print(f'[{matriz1[i][j]}]', end=' ')
    print()

print('============ MATRIZ 2 ============')

for i in range(0, 2):
    for j in range(0, 2):
        print(f'[{matriz2[i][j]}]', end=' ')
    print()

print('============ MATRIZ SOMA ============')

for i in range(0, 2):
    for j in range(0, 2):
        print(f'[{matrizsoma[i][j]}]', end=' ')
    print()

print('============ MATRIZ SUBTRAÇÃO ==================')

for i in range(0, 2):
    for j in range(0, 2):
        print(f'[{matrizsub[i][j]}]', end=' ')
    print()

print('=============== MATRIZ COM CONSTANTE ===========')

for i in range(0, 2):
    for j in range(0, 2):
        print(f'[{matrizconst[i][j]}]', end=' ')
    print()
