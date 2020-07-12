"""
42. Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e
escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize
a entrada de dados com um valor negativo ou zero.
"""
from math import sqrt

try:
    contador = 1
    while True:
        num = float(input(f'{contador} - Insira um número:  '))
        if (num < 0) or (num == 0):
            print('Programa finalizado!!!')
            break
        else:
            print(f'{contador} - O quadrado do valor lido: {num * num} - o Cubo: {num * num * num} - ' 
                  f'A raiz quadrada: {sqrt(num)}')
            contador = contador + 1
except ValueError:
    print('ERRO!!!')