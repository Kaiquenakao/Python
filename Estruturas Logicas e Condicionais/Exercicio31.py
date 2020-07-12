"""
31. Faça um programa que receba altura e o peso de uma pessoa. De acordo com a tabela
a seguir, verifique e mostra qual a classificação dessa pessoa.
------------------------------------------------------------------------
| Altura           |                       PESO                        |
|                  | Até 60 | Entre 60 e 90 (inclusive)  | Acima de 90 |
| Menor que 1,20   |   A    |            D               |     G       |
| De 1,20 a 1,70   |   B    |            E               |     H       |
| Maior que 1,70   |   C   |             F               |     I       |
"""
try:
    altura = float(input('Insira a altura em metros, por exemplo (1.20) :  '))
    peso = float(input('Insira o peso:  '))
    if (altura < 1.20) and (peso > 0) and (peso <= 60):
        print('Clasificação A')
    if (altura < 1.20) and (peso > 60) and (peso < 90):
        print('Classificação D')
    if (altura < 1.20) and (peso >= 90):
        print('Classificação G')
    if (altura >= 1.20) and (altura <= 1.70) and (peso > 0) and (peso <= 60):
        print('Clasificação B')
    if (altura >= 1.20) and (altura <= 1.70) and (peso > 60) and (peso < 90):
        print('Classificação E')
    if (altura >= 1.20) and (altura <= 1.70) and (peso >= 90):
        print('Classificação H')
    if (altura > 1.70) and (peso > 0) and (peso <= 60):
        print('Clasificação C')
    if (altura > 1.70) and (peso > 60) and (peso < 90):
        print('Classificação F')
    if (altura > 1.70) and (peso >= 90):
        print('Classificação I')
except ValueError:
    print('ERRO!!! Só pode ser digitados números')