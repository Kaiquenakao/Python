""""
48. Leia um valor inteiro em segundos, e imprima-o em hora.
"""
try:
    inteiro = int(input('Insira um valor em segundos:  '))
    print(f'O seu valor convertido em horas: {inteiro // 60 // 60}')
except ValueError:
    print('ERRO!!! O valor tem que ser números inteiros')
