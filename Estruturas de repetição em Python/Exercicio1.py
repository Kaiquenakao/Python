"""
1. Faça um programa que determine o mostre os cincos primeiros múltiplos de 3, considerando números
maiores que 0.
"""
global numero
numero = 0
lista = []
for num in range(1,5+1):
    numero = numero + 3
    lista.append(numero)
print(lista)