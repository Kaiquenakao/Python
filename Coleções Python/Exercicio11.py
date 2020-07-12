"""
11. Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade
de números negativos e a soma dos números positivos desse vetor.
"""
try:
    negativo = 0
    lista = []
    for i in range(1, 10+1):
        n = float(input(f'{i} - Insira um valor:  '))
        if n < 0:
            negativo = negativo + 1
        else:
            lista.append(n)
    print(f'A soma dos números positivos desse vetor: {sum(lista)}\nA quantidade de números '
          f'negativos é {negativo}')
except ValueError:
    print('ERRO!!! Número inválido')