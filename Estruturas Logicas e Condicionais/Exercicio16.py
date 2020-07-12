"""
16. Usando (for, if, else), escreva um programa que leia um número inteiro entre 1 a 12 e
imprima o mês correspondente a este número, isto é, janeiro se 1, fevereiro se 2, e assim
por diante.
"""
try:
    meses = (
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
        'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    )
    num = int(input('Insira um número de 1 a 12:  '))
    if (num > 0) and (num <= 12):
        for i in meses:
            y = meses[num - 1]
        print(f'Mês: {y}')
    else:
        print('ERRO!!! Só pode ser digitado de 1 a 12')
except ValueError:
    print('ERRO!!! só pode ser digitado números inteiros.')