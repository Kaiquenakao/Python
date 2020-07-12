"""
15. Faça um programa que leia um número inteiro positivo impar N e imprima todos os números
impares de 1 até N em ordem crescente.
"""
try:
    N = int(input('Insira um número positivo impar:  '))
    if (N > 0) and (N % 2 == 1):
        for i in range(1, N + 1, 2):
            print(i, end=' ')
    else:
        print('ERRO!!! O número digitado não é positivo ou não é impar')
except ValueError:
    print('ERRO')