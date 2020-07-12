"""
26. Faça um programa que calcule o desvio padrão de um vetor v contendo n = 10 números, onde m é a
média do vetor
"""
from math import sqrt

lista = []
dp = 0

for i in range(0, 9+1):
    n = int(input(f'{i+1} - Insira um valor:  '))
    lista.append(n)
ma = sum(lista) / 4
print(f'A média: {ma}')
for i in range(0, 9+1):
    dp = pow((lista[i] - ma), 2) + dp
dp = dp / 10
print(f'O desvio padrão:  {round(sqrt(dp), 2)}')