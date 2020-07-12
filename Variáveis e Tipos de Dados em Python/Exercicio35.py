"""
35. Sejam a e b os catetos de um triangulo, onde a hipotenusa é obtida pela equação
hip = √a² + b². Faça um programa que receba os valores de a e b e calcule o valor da
hipotenusa através da equação. Imprima o resultado dessa operação.
"""
import math
try:
    a = float(input('Insira o valor de a:  '))
    b = float(input('Insira o valor de b:  '))
    print(f'O valor da hipotenusa é {"%.2f" %(math.sqrt(pow(a, 2) + pow(b, 2)))}')
except ValueError:
    print('ERRO!!! o valor de a ou b tem que ser um número')