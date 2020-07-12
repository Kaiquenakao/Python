"""
17. Faça um programa que calcule e mostre a área de um trapézio . Sabe-se que:
                    A = (basemaior + basemenor) * altura / 2
"""
try:
    bma = float(input('Insira o valor da base maior:  '))
    bme = float(input('Insira o valor da base menor:  '))
    altura = float(input('Insira o valor da altura:  '))
    A = ((bma + bme) * altura) / 2
    print(f'A área do trapézio: {A}')
except ValueError:
    print('ERRO!!!! Só pode ser digitados números')