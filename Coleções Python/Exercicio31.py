"""
31. Faça um programa que leia dois vetores de 10 elementos. crie um vetor que seja a união entre
os dois vetores anteriores, ou seja, que contém os números dos dois vetores. Não deve conter números
repetidos
"""
conjuntoA = []
conjuntoB = []

print('Conjunto A')

for i in range(0, 9+1):
    n = float(input(f'Conjunto A: {i+1} - Insira um número:  '))
    conjuntoA.append(n)

print('Conjunto B')

for i in range(0, 9+1):
    n = float(input(f'Conjunto B: {i + 1} - Insira um número:  '))
    conjuntoB.append(n)

A = set(conjuntoA)
B = set(conjuntoB)

print(A.union(B))