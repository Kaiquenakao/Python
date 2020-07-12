"""
57. Faça um programa que permita ao usuário entrar com uma matriz de 3 x 3 números inteiros. Em seguida,
gere um array unidimensional pela soma dos números de cada coluna da matriz e mostrar na tela esse
array. Por exemplo, a matriz:

[5 -8 10]
[1 2  15]
[25 10 7]

[31 4 3]
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
somacolunas = []

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = float(input(f'[{[i]}] [{[j]}] Insira um número:  '))

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]}]', end=' ')
    print()

for i in range(0, 3):
    soma = 0
    for j in range(0, 3):
        soma = soma + matriz[j][i]
    somacolunas.append(soma)

print(somacolunas)