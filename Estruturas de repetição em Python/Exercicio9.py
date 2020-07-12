"""
9. Faça um programa que leia um número inteiro N e depois imprima os N primeiros
naturais ímpares.
"""
qtd = int(input('Digite a quantidade de números ímpares:'))
print([(numero * 2) + numero for numero in range(1,qtd+1)])