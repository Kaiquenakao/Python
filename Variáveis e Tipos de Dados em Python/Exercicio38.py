"""
38. Leia um salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo
que ele recebeu um aumento de 2%
"""
try:
    sal = float(input('Digite o seu salário:  '))
    print(f'O seu novo salário: {sal + (sal * 2 / 100)}')
except ValueError:
    print('ERRO!!! O valor digitado tem que ser em números')