"""
37. Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%.
"""
try:
    produto = float(input('Insira o valor do produto:  '))
    print(f'O desconto do produto é {produto - ((produto * 12) / 100)}')
except ValueError:
    print('ERRO!!!, o valor digitado tem que ser números')