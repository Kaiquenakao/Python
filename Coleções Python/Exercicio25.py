"""
25. Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que não são
múltiplos de 7 ou que terminam com 7
"""
lista = []
contador = 0
soma = 0
while True:
    contador = contador + 1
    if not contador % 7 == 0 and not contador % 10 == 7:
        lista.append(contador)
        soma = soma + 1
    if soma == 100:
        print(lista)
        break