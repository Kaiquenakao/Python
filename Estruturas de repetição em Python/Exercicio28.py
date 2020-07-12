"""
28. Faça um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E,
conforme a fórmula a seguir
    E = 1 + 1/ 1! + 1/ 2! + 1/3! + 1...+1 / N!
"""
import math
try:
    N = int(input('Insira um número inteiro e positivo:  '))
    um = 1
    soma = 0
    div = 2
    if N > 0:
        for i in range(0, N):
            if i == 0:
                soma = 1 + um
            E = soma + math.factorial(i)
            if math.factorial(0) == 1:
                E -= 1
            if i == N-1:
                E = math.factorial(N)
            if (i >= 0) and (i <= N):
                if i == 0:
                    E = 2
                if (i > 0) and (i <= N):
                    div = div / E
        print(f'O resultado da fórmula do E: {div}')
    else:
        print('ERRO!!! O número não é inteiro positivo')
except ValueError:
    print('ERRO!!!')