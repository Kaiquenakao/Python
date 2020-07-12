"""
41. Faça um programa que leia o valor da hora de trabalho (em reais) e números de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor
calculado
"""
try:
    hora = int(input('Insira o valor da hora de trabalho:  '))
    num = int(input('Insira o número de hora trabalhadas no mês:  '))
    final = num * hora
    print(f'O valor a ser pago {final} reais, adicionando 10% ao valor final fica {final + (final * 10) / 100} no final do mês')
except ValueError:
    print(f'ERRO!!! Só pode ser digitado números')