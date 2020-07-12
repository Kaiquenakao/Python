"""
17. Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuírem valores
negativos.
"""
lista = []

for i in range(1, 10+1):
    n = float(input(f'{i} - Insira um número:  '))
    if n < 0:
        lista.append(0)
    else:
        lista.append(n)
