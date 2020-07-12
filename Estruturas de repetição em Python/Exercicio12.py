"""
12. Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais
de 0 até N em ordem decrescente.
"""
try:
    num = int(input('Insira um número positivo:  '))
    if num > 0:
        for i in range(num, -1, -1):
            print(i, end=' ')
    else:
        print('ERRO!!! O número não é positivo')
except ValueError:
    print('ERRO!!!! Só pode ser digitados números inteiros positivos')