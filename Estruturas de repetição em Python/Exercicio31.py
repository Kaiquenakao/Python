"""
31. Faça um programa que calcule e escreva o valor de S

    S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50
"""
try:
    contador = 1
    soma = 0
    final = 0
    numero = int(input('Insira a sequencia:  '))
    while numero >= contador:
        if contador == 1:
            soma = 1
        if contador > 1:
            soma = soma + 2
        S = soma / contador
        contador = contador + 1
        final += S
    print(f'O resultado final é {final}')
except ValueError:
    print('ERRO!!!')