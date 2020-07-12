"""
51. Um funcionário recebe um aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996
recebeu um aumento de 1.5%. A partir de 1997, os aumentos sempre correspondem o dobro
do ano inteiror. Faça um programa que determine o salário atual do funcionário.
"""
salario = 2000
anoinicial = 1995
aumento = 1.5
ano = int(input('Qual o ano atual:  '))
while anoinicial < ano:
    print(f'Ano {anoinicial} salario {round(salario, 2)}')
    salario = (salario + (salario * aumento) / 100)
    aumento = aumento * 2
    anoinicial = anoinicial + 1
