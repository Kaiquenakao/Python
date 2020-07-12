"""
44. Leia um número positivo do usuário, então, calcule e imprima a sequência fibonnaci até
o primeiro número superior ao número lido, exemplo: se o usuário informou o número 30,
a sequência impressa será 0 1 1 2 3 5 8 13 21 34.
"""
Nant = 1
Fibonacci = 0

n = int(input('Digite um número:(Este vai ser o nº de elementos da sequência) '))

while True:
    print(Fibonacci, end=' → ')
    Fibonacci = Fibonacci + Nant
    Nant = Fibonacci - Nant
    if Fibonacci > n:
        print(Fibonacci, end=' → ')
        break