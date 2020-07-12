"""
4. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    * O número digitado ao quadrado
    * A raiz quadrada do número digitado.
"""
import math
num = float(input('Insira o seu valor:'))
if num > 0:
    print(f'O número digitado ao quadrado:{num ** 2}')
    print(f'A raiz quadrada do número digitado:{math.sqrt(num)}')