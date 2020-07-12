"""
40. Elabore um programa que faça leitura de vários números inteiros, até que e digite um
número negativo. O programa tem que retornar o maior e menor número lido.
"""
try:
    lista = []
    while True:
        num = int(input('Insira um número inteiro:  '))
        if num > 0:
            lista.append(num)
        else:
            print(f'O maior número: {max(lista)}\nO menor número: {min(lista)}')
            break
except ValueError:
    print('ERRO!!!!')