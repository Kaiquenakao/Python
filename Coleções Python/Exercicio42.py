"""
42. Faça um programa que preenche uma matriz 4 x 4 com o produto do valor da linha e da coluna de cada
elemento. Em seguida, imprima na tela a matriz.
"""
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(0, 4):
    for j in range(0, 4):
        matriz[i][j] = i * j

for i in range(0, 4):
    for j in range(0, 4):
        print(f'[{matriz[i][j]}]', end=' ')
    print()