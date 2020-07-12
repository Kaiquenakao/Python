"""
53. Escreva um programa que leia um numero inteiro positivo n e em seguida imprima n linhas
do chamado triangulo floyd. para n = 6, temos:
1
1 2
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
n = int(input('Insira a quantidade da sequência:  '))
c = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        c = c + 1
        print(c, end=' ')
    print('\n')

