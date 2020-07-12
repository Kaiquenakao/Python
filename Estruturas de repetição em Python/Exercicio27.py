"""
27. em matemática, o número harmônico designado por H(n) define-se como sendo a soma da série
harmônica:
    H(n) = 1 + 1 / 2 + 1 / 3 + 1 / 4 + ... 1 / n
faça um programa que leia um valor n inteiro e positivo e apresente o valor de H (n)
"""
from statistics import harmonic_mean
try:
    n = int(input('Insira um valor inteiro e positivo:  '))
    if n > 0:
        x = harmonic_mean([n])
    else:
        print('ERRO!!! valor inserido é negativo')
    print(f'O valor de H(n): {x}')
except ValueError:
    print('ERRO!!!!')