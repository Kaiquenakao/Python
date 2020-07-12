"""
27. Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos que são primos
e suas respectivas posições no vetor
"""
lista = []
listaelementos = []
listaposicoes = []

for i in range(0, 9+1):
    n = int(input(f'{i} - Insira um número:  '))
    lista.append(n)
    if (n == 2) or (n == 3) or (n == 5) or (n == 7):
        listaelementos.append(n)
        listaposicoes.append(i)
    if not (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n == 1):
        listaelementos.append(n)
        listaposicoes.append(i)

print(f'Os primos com suas posições e valor: {list(zip(listaposicoes, listaelementos))}')