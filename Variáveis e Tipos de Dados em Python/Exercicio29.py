"""
29. Leia quatro notas, calcule a média aritmética e imprima o resultado.
"""
soma = 0
for n in range(1, 4+1):
    notas = float(input(f'Prova {n} - insira a sua nota de 0-10:  '))
    if notas < 0 or notas > 10:
        del notas
        break
    else:
        soma = soma + notas
try:
    print(f'A média aritmetica: {soma/4}')
except NameError:
    print('Sua nota que insiriu foi maior que 10 ou menor que 0')
