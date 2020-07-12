"""
21. Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada. crie
um novo vetor denominado C calculando C = A - B. mostre na tela os dados do vetor C.
"""
vetorA = []
vetorB = []
vetorC = []

for i in range(0, 4+1):
    n = int(input(f'Vetor A - {i+1} - Insira um número:  '))
    vetorA.append(n)
print('\n')
for i in range(0, 4+1):
    n = int(input(f'Vetor B - {i+1} - Insira um número:  '))
    vetorB.append(n)
for i in range(0, 4+1):
    C = vetorA[i] - vetorB[i]
    vetorC.append(C)
print(f'Vetor A: {vetorA}\nVetor B: {vetorB}\nVetor C: {vetorC}')
