"""
25. Calcule as raízes da equação de 2º grau
lembrando que:

x = -b ± √Δ / 2a

onde

Δ = b² - 4 * a * c

A variavel A tem que ser diferente de 0. Caso seja igual, imprima a mensagem "Não é equação
de segundo grau".
    * Δ < 0, não existe real. Imprima a mensagem "Não existe raiz".
    * Δ = 0, existe uma raiz. Imprima a raiz e a mensagem "Raiz única".
    * Δ > 0, Imprima as duas raíze reais.
"""
import math
try:
    a = float(input('Insira o valor de A:  '))
    if a == 0:
        print('Não é uma equação de segundo grau.')
        exit()
    b = float(input('Insira o valor de B:  '))
    c = float(input('Insira o valor de C:  '))
    delta = (b * b) - 4 * a * c
    print(f'Valor do delta: {delta}')
    if delta < 0:
        print("Não existe raiz")
    if delta == 0:
        x1 = ((- b + math.sqrt(delta)) / (2 * a))
        x2 = ((- b - math.sqrt(delta)) / (2 * a))
        print(x1)
        print(x2)
        print('Raiz única')
    if delta > 0:
        x1 = ((- b + math.sqrt(delta)) / (2 * a))
        print(x1)
        x2 = ((- b - math.sqrt(delta)) / (2 * a))
        print(x2)
except ValueError:
    print('ERRO!!! só pode ser digitados números')