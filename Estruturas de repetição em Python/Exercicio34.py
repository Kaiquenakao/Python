"""
34. Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20?
ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar
resto.
"""
try:
    numero = 1
    divisor = 0
    cont = 0

    while numero > 0:
        divisor = 1
        cont = 0
        while divisor <= 20:
            if numero % divisor == 0:
                cont += 1
                divisor +=1
    if cont == 20:
        numero += 1
        print(numero)
except ValueError:
    print('ERRO!!! Número digitado inválido')