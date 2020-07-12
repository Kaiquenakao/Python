""""
41. Faça um algoritmo que calcule o imc de uma pessoa e mostre sua classificação de acordo
com a tabela abaixo
---------------------------------------------------------
|        IMC             | Classificação                |
|      < 18,5            | Abaixo do peso.              |
|      18,5 - 24,9       | Saudavel                     |
|      25,0 - 29,9       | Peso em excesso              |
|      30,0 - 34,9       | Obesidade Grau |             |
|      35,0 - 39,9       | Obesidade Grau || (severa)   |
|      >= 40,0           | Obesidade Grau ||| (mórbida) |
"""
try:
    peso = float(input('Qual é seu peso ? (Kg)  '))
    altura = float(input('Qual é a sua altura? (m) '))
    imc = peso / (altura ** 2)
    if (imc > 0) and (imc < 18.5):
        print(f'O seu imc é {imc}\nAbaixo do peso')
    if (imc >= 18.5) and (imc <= 24.9):
        print(f'O seu imc é {imc}\nSaudável')
    if (imc >= 25.0) and (imc <= 29.9):
        print(f'O seu imc é {imc}\nPeso em excesso')
    if (imc >= 30.0) and (imc <= 34.9):
        print(f'O seu imc é {imc}\nObesidade Grau |')
    if (imc >= 35.0) and (imc <= 39.9):
        print(f'O seu imc é {imc}\nObesidade Grau || (severa)')
    if imc >= 40.0:
        print(f'O seu imc é {imc}\nSaudável')
except ValueError:
    print('ERRO!!!!')