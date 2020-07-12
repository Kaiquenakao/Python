"""
31. Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
"""
try:
    inteiro = int(input('Insira um número inteiro:  '))
    print(f'O número sucessor digitado: {inteiro + 1}\nO número antecessor digitado: {inteiro -1}')
except ValueError:
    print(f'Erro!! Você digitou um número que não é inteiro')