"""
57. Faça um programa que conte quantos números primos existem entre a e b, onde a e b são números
informados pelo usuário.
"""
a = int(input('Insira um número:  '))
b = int(input('Insira um número:  '))

lista = []
impar = 0

if b > a:
    for i in range(a+1, b):
        if i == 2 or i == 3 or i == 5 or i == 7:
            lista.append(i)
        if not (i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0):
            lista.append(i)
    print(lista)
else:
    print('Valor de B tem que ser maior que A!!')