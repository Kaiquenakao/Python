"""
13. Faça um programa que leia um número inteiro positivo par N e imprima todos os números
pares de 0 até N em ordem crescente.
"""
try:
    num = int(input('Insira um número positivo par:  '))
    if (num % 2 == 0) and (num > 0):
        for i in range(0, num + 1, 2):
            print(i, end=' ')
    else:
        print('ERRO!!! O número não é positivo ou não é par')
except ValueError:
    print('ERRO!!! Só pode ser digitado números')