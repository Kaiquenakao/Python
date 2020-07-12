"""
30. Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção
entre 2 vetores anteriores, ou seja, que contém apenas os números que estão em ambos vetores.
"""
conjuntoA = []
conjuntoB = []

print('Conjunto A')

for i in range(0, 9+1):
    n = float(input(f'Conjunto : {i+1} - Insira um número:  '))
    conjuntoA.append(n)

print('Conjunto B')

for i in range(0, 9+1):
    n = float(input(f'Conjunto B: {i + 1} - Insira um número:  '))
    conjuntoB.append(n)

A = set(conjuntoA)
B = set(conjuntoB)

print(A.intersection(B))