"""
32. Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como saída
o número de cada dado e a relação entre eles (> , <, =) de cada lançamento
"""
import random
try:
    n = int(input('Insira o número de vezes que os dados irão rolar:  '))
    for i in range(1, n+1):
        d1 = random.randint(1, 6)
        d2 = random.randint(1,6)
        if d1 > d2:
            print(f'{i} rodada - O dado 1:({d1}) é maior que o dado 2: ({d2})')
        if d1 < d2:
            print(f'{i} rodada - O dado 2: ({d2}) é maior que o dado 1: ({d1})')
        if d1 == d2:
            print(f'{i} rodada - ambos os dados são iguais, sendo dado 1: ({d1}) e dado 2: ({d2})')
except ValueError:
    print('ERRO!!! Número inválido')