""""
34. Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
A área do círculo é pi * raio², considere o pi = 3.141592.
"""
try:
    pi = 3.141592
    raio = float(input('Insira o valor do raio:  '))
    print(f'A área do círculo é {"%.2f" % (pi * (raio * raio))}')
except ValueError:
    print(f'Erro!!! Só pode ser digitado números')