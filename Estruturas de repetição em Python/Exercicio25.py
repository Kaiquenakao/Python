"""
25. Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3
ou 5
"""
try:
    soma = 0
    for i in range(1, 1000):
        if (i % 3 == 0) or (i % 5 == 0):
            soma = soma + i
    print(f'A soma dos múltiplos de 3 ou 5 abaixo de 1000: {soma}')
except ValueError:
    print('ERRO!!!')