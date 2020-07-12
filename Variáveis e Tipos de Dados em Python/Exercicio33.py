"""
33. Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.
"""
try:
    lado = float(input('Insira o tamanho do lado do quadrado:  '))
    print(f'A área do quadrado é igual a {lado * lado}')
except ValueError:
    print(f'Erro!!! Só pode ser digitado números')