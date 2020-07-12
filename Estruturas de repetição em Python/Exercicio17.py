"""
17. Faça um programa que leia um número inteiro positivo N e calcule a soma dos N primeiros
números naturais
"""
try:
    N = int(input('Insira um número inteiro positivo:  '))
    soma = 0
    if N > 0:
        for i in range(1, N+1):
            soma = soma + i
        print(f'A soma dos primeiros numeros naturais: {soma}')
    else:
        print('ERRO!!! O número não é positivo')
except ValueError:
    print('ERRO!!! O número digitado precisa ser inteiro')