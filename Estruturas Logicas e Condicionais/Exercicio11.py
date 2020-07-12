""""
11. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a
soma de todos os seus algarimos. Por exemplo, ao numero 251 corresponderá o valor 8
( 2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará com a mensagem
"número invalido".
"""
try:
    numero = int(input("Informe um número inteiro:  "))
    if numero > 0:
        soma = 0
        while numero > 0:
           soma += numero % 10
           numero = numero // 10
        print(soma)
    else:
        print('Número invalido')
except ValueError:
    print('ERRO!!! Só pode ser digitados números inteiros')