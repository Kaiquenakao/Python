"""
26. Faça um que encontre o primeiro multiplo de 11, 13 ou 17 após um número dado.
"""
try:
    num = int(input('Insira um número:  '))
    if num % 11 == 0:
        print('Multiplo de 11')
        exit()
    if num % 13 == 0:
        print('Multiplo de 13')
        exit()
    if num % 17 == 0:
        print('Multiplo de 17')
        exit()
except ValueError:
    print('ERRO')