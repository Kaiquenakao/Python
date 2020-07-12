"""
54. Faça um programa que receba um número inteiro maior do que 1, e verifique se o número
fornecido é primo ou não
"""
n = int(input('Insira um número:  '))
contador = 0
if n > 1:
    for i in range(1, n + 1):
        if n % i == 0:
            contador += 1
    if contador == 2:
        print(f'O número {n} é primo')
    else:
        print(f'O número {n} não é primo')
else:
    print('ERRO!!!')
    exit()