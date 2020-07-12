"""
33. Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com
valor zero. para isso, todos os elementos à frente do valor zero, devem ser movidos uma posição atras
no vetor.
"""
lista = []
for i in range(0, 14+1):
    n = float(input(f'{i+1} - Insira um número:  '))
    lista.append(n)

for i in lista:
    if i == 0:
        lista.remove(i)

print(f'{lista}')