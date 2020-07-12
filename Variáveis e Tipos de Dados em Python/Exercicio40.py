"""
40. Uma empresa contrata um encanador por R$ 30,00 por dia. Faça um programa que solicite
o número dos dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontado 8% para imposto de renda.
"""
try:
    dias = int(input('Insira a quantidade de dias trabalhos do encanador:  '))
    salario = dias * 30
    print(f'O salario líquido: {salario - (salario * 8) / 100}')
except ValueError:
    print('ERRO!!! os dias tem que ser um número inteiro')