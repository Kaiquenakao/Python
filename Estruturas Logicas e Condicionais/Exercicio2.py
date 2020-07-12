"""
2. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""
import math
num = int(input('Insira um número:'))
if num >= 0:
    print(f'A raiz do número:{math.sqrt(num)}')
else:
    print('Número inválido')