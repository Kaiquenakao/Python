"""
28. Leia 10 números inteiros e armazene em um vetor v, crie dois novos vetores v1 e v2. Copie os
valores ímpares de v para v1, e os pares de v para v2. Note que cada um dos vetores v1 e v2 têm no
maximo 10 elementos, mas nem todos os elementos são utilizados. No final escreva os elementos
utilizados de v1 e v2
"""
vetorV = []
v1 = []
v2 = []
for i in range(0, 9+1):
    n = int(input(f'{i+1} - Insira um número:  '))
    vetorV.append(n)

for i in range(0, 9+1):
    if vetorV[i] % 2 == 0:
        v2.append(vetorV[i])
    else:
        v1.append(vetorV[i])
print(f'O Vetor impares v1: {v1}\nO vetor pares v2: {v2}')
