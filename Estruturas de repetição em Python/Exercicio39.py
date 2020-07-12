"""
39. Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas
pelo usuário. Esse programa não pode permitir a entrada de dados inválidos, ou seja, medidas
menores ou iguais a 0.
"""
try:
    base = float(input('Insira o valor da base:  '))
    altura = float(input('Insira o valor da altura:  '))
    if (base > 0) and (altura > 0):
        area = (base * altura) / 2
        print(f'A area do triângulo: {area}')
    else:
        print('Dados inválidos')
except ValueError:
    print('ERRO!!!!')