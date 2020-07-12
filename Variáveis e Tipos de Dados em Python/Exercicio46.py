"""
46. Faça um programa que leia um número inteiro positivo de três digitos (de 100 a 999),
Gere outro número formado pelos dígitos invertidos do número lido
"""
try:
    valor = int(input('Insira um três digitos inteiros (de 100 a 999):  '))
    if (valor >= 100) and (valor <= 999):
        x = str(valor)
        print(x[::-1])
    else:
        print('ERRO!!! Você não digitou os digitos inteiros (de 100 a 999)')
except ValueError:
    print('ERRO!!! o valor digitado tem que ser inteiro')