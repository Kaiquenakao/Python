"""
41. Declare um matriz 5 x 5. Preencha com a 1 diagonal principal e com 0 os demais elementos.
Escreva ao final a matriz obtida
"""
matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i in range(0, 5):
    for j in range(0, 5):
        if i == j:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0

for i in range(0, 5):
    for j in range(0, 5):
        print(f'[{matriz[i][j]}]', end=' ')
    print()