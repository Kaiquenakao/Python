"""
52. Gere matriz 4 x 4 com valores no intervalo [1, 20]. Escreva um programa que transforme a matriz
gerada numa matriz triangular inferior, ou seja atribuindo zero a todos os elementos acima da
diagonal principal. Imprima a matriz original e a matriz transformada.
"""
import random
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(0, 4):
    for j in range(0, 4):
        matriz[i][j] = random.randint(1, 20)

print('\n-----------------Matriz Original----------------\n')

for i in range(0, 4):
    for j in range(0, 4):
        print(f'[{matriz[i][j]}]', end=' ')
    print()

print('\n-----------------Matriz Transformada-------------\n')

for i in range(0, 4):
    for j in range(0, 4):
        if i > j:
            matriz[i][j] = 0
        print(f'[{matriz[i][j]}]', end=' ')
    print()

