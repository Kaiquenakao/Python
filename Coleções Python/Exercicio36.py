"""
36. Leia um vetor com 10 números reais, ordene os elementos deste vetor, e no final escreva os
elementos do vetor ordenado.
"""
vetor = []

for i in range(0, 9+1):
    n = float(input(f'{i+1} - Insira um número:  '))
    vetor.append(n)

print(sorted(vetor))