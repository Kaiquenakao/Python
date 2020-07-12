"""
18. Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e
quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser
fornecido pelo usuário.
"""
try:
    qnt = int(input('Insira quantos números você quer digitar:  '))
    lista = []
    contador = 0
    for i in range(1, qnt+1):
        num = int(input(f'{i} - Insira um número:  '))
        lista.append(num)
    maior = max(lista)
    for i in lista:
        if max(lista) == i:
            contador = contador + 1
    print(f'O número maior é {maior} e ele foi repetido {contador} vezes')
except ValueError:
    print('ERRO!!!')