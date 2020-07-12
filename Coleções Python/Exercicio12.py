"""
12. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente
com o maior, o menor e a média dos valores.
"""
lista = []
for i in range(1, 5+1):
    n = float(input(f'{i} - Insira um número:  '))
    lista.append(n)
print(f'O maior valor lido: {max(lista)}\nO menor valor lido: {min(lista)}\nA média dos valores:  {sum(lista) / 5}')