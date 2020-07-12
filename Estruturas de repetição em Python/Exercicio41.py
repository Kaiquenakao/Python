"""
41. Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos
pelo usuário via teclado. O programa fica pedindo estes valores e calculando até que o
usuário entre com um valor para resistência igual a zero.
"""
try:
    R1 = float(input('Insira um valor para o R1:  '))
    R2 = float(input('Insira um valor para o R2:  '))
    if (R1 == 0) or (R2 == 0):
        print(f'ERRO!!! Resistência igual a zero')
        exit()
    else:
        R = (R1 * R2) / (R1 + R2)
    print(f'O valor do R: {round(R, 2)}')
except ValueError:
    print('ERRO!!!!')