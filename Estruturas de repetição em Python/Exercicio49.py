"""
49. O funcionário chamado Carlos tem um colega chamado joão que recebe um salário que equivale
a um terço do seu salário. Carlos gosta de fazer aplicações na caderneta de poupança e vai
aplicar seu salário integralmente nela, pois está rendendo 2% ao mês.
João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 5% ao mês.
Construa um programa que deverá calcular e mostrar a quantidade de meses necessários para
que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos. Teste
com outros valores para as taxas.
"""

salcarlos = float(input('Insira o valor do salário do Carlos:  '))
saljoao = round((salcarlos / 3), 2)

mes = 1
while True:
    salcarlos = salcarlos * 1.02
    saljoao = round((saljoao * 1.05), 2)
    mes = mes + 1
    if (saljoao == salcarlos) and (saljoao > salcarlos):
        print(f'A quantidade meses para ultrapassar ou igualar é {mes}')
        break
