"""
15. Usando (if, else, elif), escreva um programa que leia um inteiro entre 1 e 7 e imprima
o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e
assim por diante.
"""
try:
    dias = ('Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabádo')
    num = int(input('Insira um número de 1 a 7:  '))
    if (num > 0) and (num <= 7):
        for i in dias:
            y = dias[num - 1]
        print(y)
    else:
        print('ERRO!!! Só pode ser digitado de 1 a 7')
except ValueError:
    print('ERRO!!! só pode ser digitado números inteiros.')