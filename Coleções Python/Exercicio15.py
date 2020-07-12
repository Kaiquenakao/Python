"""
15. Leia um vetor de 20 números inteiros. Escreva os elementos eliminando elementos repetidos
"""

lista = []
repetidos = []

for i in range(1, 10):
    n = float(input('Insira um valor:  '))
    if n not in lista:
        lista.append(n)
    else:
        lista.remove(n)
print(f'Os valores: {lista}')