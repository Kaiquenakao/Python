"""
23. Faca um algoritmo que leia um número positivo inteiro e imprima uma lista de seu divisores.
"""
try:
    lista = []
    num = int(input('Insira um número:  '))
    for i in range(1, num + 1):
        if num % i == 0:
            lista.append(i)
    print(lista)
except ValueError:
    print('ERRO!!!!!')