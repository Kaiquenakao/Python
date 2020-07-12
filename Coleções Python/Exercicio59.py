"""
59. Faça programa que leia uma matriz 3 x 6 com valores reais.

(a) Imprima a soma de todos os elementos das colunas ímpares.
(b) Imprima a média aritmética dos elementos da segunda e quarta coluna.
(c) imprima um novo vetor que contém a soma dos valores das colunas 1 e 2.

"""

matriz = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
contador = 0
linha = 0
coluna = 0
soma = 0
somasequa = 0
somaumdois = 0
vetor = []
test = []
somatest = 0
for i in range(0, 3):
    for j in range(0, 6):
        matriz[i][j] = int(input(f'Linha: {i} - Coluna: {j} Insira um número:  '))

for i in range(0, 3):
    for j in range(0, 6):
        print(f'[{matriz[i][j]}]', end=' ')
        if (j+1) % 2 != 0:
            soma = matriz[i][j] + soma
        if j == 1 or j == 3:
            somasequa = somasequa + matriz[i][j]
    print()

for li in range(0, 3):
    somaumdois = 0
    for c in range(0, 2):
        somaumdois = somaumdois + matriz[li][c]
    vetor.append(somaumdois)

print(f'(a) Soma das colunas ímpares: {soma}\n(b) Média aritmética da segunda e quarta coluna:  {somasequa/2}'
      f'\n(c) Vetor da soma da coluna 1 e 2: {vetor}')

