"""
12. Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido".
Se o número for positivo, calcular o logaritmo deste número.
"""
import math
num = int(input('Insira números:  '))
if num > 0:
    print(math.log(num))
else:
    print('Número inválido')