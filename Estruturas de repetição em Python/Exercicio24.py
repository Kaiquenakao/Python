"""
24. Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores
desse número, com exceção dele próprio. Ex: A soma dos divisores do número 66 é 1 + 2
+ 3 + 6 + 11 + 22 + 33 = 78
"""
try:
    lista = []
    num = int(input('Insira um número:  '))
    for i in range(1, num):
        if num % i == 0:
            lista.append(i)
    print(f'A soma dos divisores do número {num} é {sum(lista)}')
except ValueError:
    print('ERRO!!!!')
