"""
8. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
"""
lista = []
for num in range(1,10+1):
    numeros = float(input(f'Posição{num}:Digite o seu número:'))
    lista.append(numeros)
print(f'O maior valor lido:{max(lista)}\nO menor valor lido:{min(lista)}')