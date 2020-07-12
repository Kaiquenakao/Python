"""
18. Faça um programa que leia um vetor de 10 números. Leia um número x, conte os múltiplos de um
número inteiro x num vetor e mostre-os na tela.
"""
lista = []
mult = 0
for i in range(1, 10+1):
    n = float(input(f'{i} - Insira um número:  '))
    lista.append(n)
    if i == 10:
        x = float(input('Insira um valor:  '))
for i in lista:
    if i % x == 0:
        mult = mult + 1
print(f'Existem {mult} multiplos do {x}')

