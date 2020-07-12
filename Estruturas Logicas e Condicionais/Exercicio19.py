"""
19. Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou
5, mas não simultaneamente pelos dois
"""
try:
    num = int(input('Insira um valor:  '))
    if (num % 3 == 0) and (num % 5 == 0):
        exit()
    if num % 3 == 0:
        print('Número divisível por 3')
    if num % 5 == 0:
        print('Número divisível por 5')
except ValueError:
    print('ERRO!!! Só pode ser digitado números inteiros')