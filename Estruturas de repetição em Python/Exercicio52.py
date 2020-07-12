"""
52. Escreva um programa que receba com entrada o valor do saque realizado pelo cliente
de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a
menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
"""
try:
    saque = int(input("informe o valor do saque (numero inteiro): "))
    nota100 = saque // 100
    saque %= 100
    nota50 = saque // 50
    saque %= 50
    nota20 = saque // 20
    saque %= 20
    nota10 = saque // 10
    saque %= 10
    nota5 = saque // 5
    saque %= 5
    nota2 = saque // 2
    saque %= 2
    nota1 = saque // 1
    saque %= 1
    print(f'Você utilizou {nota100} notas de 100 reais\nVocê utilizou {nota50} notas de 50 reais\n'
          f'Você utilizou {nota20} notas de 20 reais\nVocê utilizou {nota5} notas de 5 reais\n'
          f'Você utilizou {nota2} notas de 2 reais\nVocê utilizou {nota1} notas de 1 real')
except ValueError:
    print('ERRO!!! Número invalido')