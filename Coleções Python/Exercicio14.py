"""
14. Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os
escreva na tela
"""

lista = []
repetidos = []

for i in range(1, 10):
    n = float(input('Insira um valor:  '))
    if n not in lista:
        lista.append(n)
    else:
        repetidos.append(n)
print(f'Os valores: {repetidos} são repetidos')