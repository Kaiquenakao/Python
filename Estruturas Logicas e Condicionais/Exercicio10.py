"""
10. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes fórmulas(onde h corresponde à a altura)
    Homens = (72.7 * h) - 58
    Mulheres = (62.1 * h) - 44.7
"""
altura = float(input('Insira a sua altura:'))
sexo = input('Insira o seu sexo. Homem ou mulher:')
if sexo == 'Homem':
    peso = (72.7 * altura) - 58
if sexo == 'Mulher':
    peso = (62.1 * altura) - 44.7
print(f'O seu peso ideal:{peso}')