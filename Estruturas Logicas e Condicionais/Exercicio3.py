"""
3. Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima
o número ao quadrado
"""
import math
num = float(input('Insira o seu valor:'))
if num >= 0:
    print(f'A raiz quadrada:{math.sqrt(num)}')
else:
    print(f'Número ao quadrado:{num ** 2}')