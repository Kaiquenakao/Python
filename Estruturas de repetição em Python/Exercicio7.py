"""
7. Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua
média
"""
global soma
soma = 0
media = 0
for num in range(1,10+1):
    numero = int(input(f'Posição{num}:digite o seu número:'))
    if numero > 0:
        soma = soma + numero
        media = media + 1
print(f'Média:{soma/media}')