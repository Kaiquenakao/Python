"""
11. Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais
de 0 até N em ordem crescente
"""
try:
    num = int(input('Insira um número inteiro positivo:  '))
    if num > 0:
        for i in range(0, num + 1):
            print(i, end=' ')
    else:
        print('ERRO!!! o número inteiro tem que ser positivo')

except ValueError:
    print('ERRO!!!! Só pode ser digitado números inteiros')