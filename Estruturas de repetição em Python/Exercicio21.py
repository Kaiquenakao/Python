"""
21. Faça um programa que receba dois números inteiros. Calcule e mostre:
    º A soma dos números pares desse intervalo de números, incluindo os números digitados;
    ° A multiplicação dos números ímpares desse intervalo, incluindo os digitados;
"""
try:
    a = int(input('Insira o primeiro número:  '))
    b = int(input('Insira o segundo número:  '))
    somapar = 0
    multimpar = 1
    if a > b:
        for i in range(b, a + 1):
            if i % 2 == 0:
                somapar = somapar + i
            elif i % 2 == 1:
                multimpar = i * multimpar
    if b > a:
        for i in range(a, b + 1):
            if i % 2 == 0:
                somapar = somapar + i
            if i % 2 == 1:
                multimpar = i * multimpar
    print(f'Soma dos pares {somapar}\nMultiplicação dos impares {multimpar}')
except ValueError:
    print('ERRO!!!')