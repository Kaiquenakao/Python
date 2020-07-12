"""
22. Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo, nas posições
pares os valores do primeiro e nas posições impares os valores do segundo.
"""
vetorA = []
vetorB = []
vetorC = []
print('Vetor 1')
for i in range(0, 9+1):
    n = int(input(f'{i+1} - Insira um número:  '))
    vetorA.append(n)
print('Vetor 2')
for i in range(0, 9+1):
    n = int(input(f'{i+1} - Insira um número:  '))
    vetorB.append(n)
for i in range(0, 9+1):
    if i % 2 == 0:
        c = vetorB[i]
        vetorC.append(c)
    else:
        c = vetorA[i]
        vetorC.append(c)
print(vetorA)
print(vetorB)
print(vetorC)