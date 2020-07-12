"""
20. Escreva um que leia número inteiro inteiros no intervalo de [0, 50] e os armazene em um vetor
com 10 posições. Preencha um segundo vetor apenas com os números impares do primeiro vetor. Imprima
os dois vetores, 2 elementos por linha
"""
lista = []
listaimpar = []
impar = 0
for i in range(1, 50+1):
    n = int(input(f'{i} - Insira um número:  '))
    lista.append(n)
    if n % 2 == 1:
        impar = impar + 1
        if (impar > 0) and (impar <= 10):
            listaimpar.append(n)
        else:
            print('Lista impar cheia!!!')
print(f'A Lista de 50 vetores:  {lista}')
print(f'A Lista dos impares:  {listaimpar}')
