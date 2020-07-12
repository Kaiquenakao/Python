"""
6. Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser
impresso o maior e o menor elemento do vetor.
"""
lista = []
for i in range(1,10+1):
    numeros = float(input(f'Posição{i}:Insira um valor:'))
    lista.append(numeros)

print(f'O Vetor: {lista}\nO maior elemento do vetor:{max(lista)}\nO menor elemento do vetor:{min(lista)}')
