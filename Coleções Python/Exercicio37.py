"""
37. Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 > A7 > A8 >.... >A11, ou seja,
está ordenado em ordem crescente até o sexto elemento, e a partir desse elemento está ordenado em
ordem descrescente. dado o vetor da questão anterior, proponha um algoritmo para ordenar os elementos.
"""
vetorcrescente = []
vetordescrescente = []

for i in range(0, 5+1):
    n = float(input(f'{i+1} - Insira um número:  '))
    vetorcrescente.append(n)

for i in range(6, 10+1):
    n = float(input(f'{i + 1} - Insira um número:  '))
    vetordescrescente.append(n)

print(vetorcrescente + list(reversed(sorted(vetordescrescente))))