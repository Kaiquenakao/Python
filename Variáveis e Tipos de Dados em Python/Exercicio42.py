"""
43. Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se
que esse funcionário tem uma gratificação de 5% sobre o salário-base. além disso, ele paga
7% de imposto sobre o salário-base
"""
try:
    salario = float(input('Insira o valor do sálario base:  '))
    grati = salario * 0.05
    imposto = salario * 0.07
    print(f'O novo salário: {salario + grati - imposto}')
except ValueError:
    print(f'ERRO!!! Só pode ser digitado números')