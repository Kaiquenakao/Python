""""
2. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
"""
lista = []
for num in range(1,6+1):
    carrinho = int(input(f'Posição{num}:Insira um valor inteiro:'))
    lista.append(carrinho)
print(lista)