"""
43. Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando
for informado a idade 0), e calcule a idade média desse grupo
"""

contador = 1
soma = 0

while True:
    idade = int(input(f'{contador} - Insira uma idade:  '))
    if idade == 0:
        print('Programa finalizado')
        break
    else:
        soma += idade
        contador = contador + 1

print(f'A média desse grupo é: {soma / (contador - 1)}')