"""
28. Faça um programa que leia três números inteiros positivos e efetua o cálculo de uma
das seguintes médias de acordo com um valor númerico digitado pelo usuário:

1 - Geométrica: ³√ x * y * z
2 - Ponderada: x + 2 * y + 3 * z / 6
3 - Harmônica: 1 / 1/x + 1/y + 1/z
4 - Aritmética: x + y + z / 3
"""
from statistics import geometric_mean, harmonic_mean, mean
opcao = int(input('Opções\n1 - Geométrica: ³√ x * y * z\n2 - Ponderada: x + 2 * y + 3 * z / 6\n'
                  '3 - Harmônica: 1 / 1/x + 1/y + 1/z\n4 - Aritmética: x + y + z / 3\n'
                  'Insira a opção:  '))
if (opcao > 0) and (opcao <= 4):
    x = float(input('Insira um valor para x:  '))
    y = float(input('Insira um valor para y:  '))
    z = float(input('Insira um valor para z:  '))
    if opcao == 1:
        geo = geometric_mean([x, y, z])
        print(f'Média Geométrica: {round(geo, 2)}')
    if opcao == 2:
        pon = (x + (2 * y) + (3 * z)) / 6
        print(f'Media Ponderada: {round(pon, 2)}')
    if opcao == 3:
        har = harmonic_mean([x, y, z])
        print(f'Média harmônica: {round(har, 2)}')
    if opcao == 4:
        print(f'Média aritmética: {round(mean([x, y, z]), 2)}')
else:
    print('ERRO!!! Opção invalido')