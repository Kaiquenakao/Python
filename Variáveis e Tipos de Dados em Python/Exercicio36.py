"""
36. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
do cilindro circular é calculado por meio da segunda fórmula: V = pi * raio² * altura,
onde pi = 3.141592.
"""
pi = 3.141592
try:
    H = float(input('Insira o valor da altura:  '))
    R = float(input('Insira o valor do raio:  '))
    print(f'O volume do cilindro {"%.2f" % (H * R * R * pi)}')
except ValueError:
    print(f'ERRO!!! Altura e o raio precisam ser números')