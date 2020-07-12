"""
13. Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior
e o menor valor.
"""

maior = 0
menor = 0
posicaomaior = 0
posicaomenor = 0

for i in range(1, 5 + 1):
    n = float(input(f'{i} - Insira um número:  '))
    if i == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
            posicaomaior = i
        if n < menor:
            menor = n
            posicaomenor = i
print(f'O maior valor:  {maior} - Posisão {posicaomaior}\nO menor valor:  {menor} - Posição {posicaomenor}')