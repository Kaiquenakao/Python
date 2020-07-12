"""
40. Leia uma matriz de 4x4, conte e escreva quantos valores maiores que 10 ela possui.
"""
soma = 0
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(0, 4):
    for c in range(0, 4):
        matriz[i][c] = float(input(f'Digite um valor para [{i+1}, {c+1}]:  '))
        if matriz[i][c] > 10:
            soma = soma + 1

for i in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[i][c]}]', end=' ')
    print()

print(f'\nA matriz 4x4 possui: {soma} valores maiores que 10')