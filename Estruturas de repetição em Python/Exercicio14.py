"""
14. Faça um programa que leia um número inteiro positivo par N e imprima todos os números
pares de 0 até N em ordem decrescente
"""
try:
    N = int(input('Insira um número positivo inteiro par:  '))
    if (N > 0) and (N % 2 == 0):
        for i in range(N, -1, -2):
            print(i, end=' ')
    else:
        print('ERRO!!! O número é negativo ou não é par')
except ValueError:
    print('ERRO!!! Só pode ser digitado número negativo')