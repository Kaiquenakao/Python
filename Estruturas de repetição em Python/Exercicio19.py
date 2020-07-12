"""
19. Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída
cada um dos algorismos que compõem o número
"""
try:
    num = int(input('Insira um número entre 100 e 999:  '))
    if (num > 100) and (num < 999):
        numero = num
        for i in str(numero):
            print(int(i))
    else:
        print('ERRO!!! O número digitado não está entre 100 e 999')

except ValueError:
    print('ERRO!!!')