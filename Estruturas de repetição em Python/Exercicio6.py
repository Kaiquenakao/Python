"""
6. Faça um programa que leia 10 inteiros e imprima a sua média.
"""
import statistics
lista = []
for num in range(1,10+1):
    numero = int(input(f'Posição{num}:digite o seu número:'))
    lista.append(numero)
res = statistics.mean(lista)
print(res)