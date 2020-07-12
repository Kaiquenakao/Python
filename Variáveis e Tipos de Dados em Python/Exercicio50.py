"""
50. Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua
idade atual
"""
try:
    atual = 2020
    ano = int(input('Insira a sua idade atual:  '))
    data = atual - ano
    print(data)
except ValueError:
    print('ERRO!!, Só pode ser digitado números inteiros')