"""
48. Faça um programa que some os termos de valor par da sequência Fibonnaci, cujos valores
não ultrapassem quatro milhões.
"""
try:

    Fibonacci = 0
    Nant = 1
    soma = 0

    while True:
        print(Fibonacci, end=' → ')
        Fibonacci = Fibonacci + Nant
        Nant = Fibonacci - Nant
        if Fibonacci % 2 == 0:
            soma += Fibonacci
        if Fibonacci > 4000000:
            break
    print(f'\nA soma dos valores pares do Fibonnaci (sem passar do valor 4 milhoes): {soma}')
except ValueError:
    print('ERRO!!!')