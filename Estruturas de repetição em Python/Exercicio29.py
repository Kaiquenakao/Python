"""
29. Escreva um programa para calcular o valor da série, para os 5 termos.
    S = 0 + 1/2! + 2/4! + 3/ 6! + 4 /8! + 5.
"""
import math
div = 1
try:
    for i in range(1, 5+1):
        if i == 1:
            S = 1
        if (i > 1) and (i <= 5):
            if i == 1:
                S = math.factorial(2) + i
            else:
                S = math.factorial((2 * i) - 2) + i
        div = div / S
    print(f'O resultado do S é {div}')



except ValueError:
    print('ERRO!!!')