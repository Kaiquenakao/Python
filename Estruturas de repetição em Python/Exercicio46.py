"""
46. Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar acertar
qual o número foi gerado, a cada tentativa o programa deverá informar se o chute é menor ou
maior que o número gerado. O programa acaba quando o usuário acerta o número gerado.
O programa deve informar quantas tentativas o número foi descoberto
"""
import random

x = random.randint(1, 1000)
contador = 0

while True:
    num = int(input('Insira um valor:  '))
    if num < x:
        print('O número insirido é maior que o número aleatório!!!')
        contador = contador + 1
    if num > x:
        print('O número insirido é menor que o número aleatório!!!')
        contador = contador + 1
    if num == x:
        contador = contador + 1
        print('Você acertou!!!')
        break

print(f'O número de tentaivas: {contador}')