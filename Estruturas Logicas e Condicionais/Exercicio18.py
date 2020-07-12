"""
18. Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas
(as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede
dois valores numéricos e realiza a operação, mostrando o resultado e saindo.
"""
try:
    num = int(input('1 - Soma\n2 - Multiplicação\n3 - Divisão\n4 - Subtração\nDigite um valor:  '))
    if (num > 0) and (num <= 4):
        a = float(input('Insira o primeiro valor numérico:  '))
        b = float(input('Insira o segundo valor numérico:  '))
        if num == 1:
            print(f'O resultado da soma {a + b}')
        if num == 2:
            print(f'O resultado da multiplicação: {a * b}')
        if num == 3:
            print(f'O resultado da divisão: {a / b}')
        if num == 4:
            print(f'O resultado da subtração: {a - b}')
except ValueError:
    print('ERRO!!! Só pode ser digitado números inteiros')