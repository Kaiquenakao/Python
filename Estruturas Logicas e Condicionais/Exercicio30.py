"""
30. Faça um programa que receba três números e mostre-os em ordem crescente.
"""
try:
    num = float(input('Insira um valor:  '))
    num2 = float(input('Insira um valor:  '))
    num3 = float(input('Insira um valor:  '))
    lista = [num, num2, num3]
    lista.sort()
    print(f'Ordem crescente: {lista}')
except ValueError:
    print('ERRO!!! Só pode ser digitados números')