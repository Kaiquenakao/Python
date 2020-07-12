"""
30. Faça programas para calcular as seguintes sequências:
    1 + 2 + 3 + 4 + 5...+ n
    1 - 2 + 3 - 4 + 5 - 6... + (2n - 1)
    1 + 3 + 5 + 7+...+(2n-1)
"""
try:
    primeiro = int(input('Insira um numero inteiro positivo:  '))
    soma = 0
    somadois = 0
    final = 0
    somatres = 0
    contador = 0
    i = 0
    for i in range(1, primeiro+1):
        soma += i
    print(f'O primeiro resultado é {soma}')

    for i in range(1, primeiro + 1):
        if i == 1:
            somadois = i - (i + i)
        if (i > 1) and (i < primeiro):
            somadois += (i + 1) - (i + 2)
        if i == primeiro:
            somadois = somadois + ((2 * primeiro) - 1)
    print(f'O segundo resultado é {somadois}')

    while contador < primeiro:
        if contador == 0:
            final = 1
            somatres = final
        if (contador > 0) and (contador < primeiro):
            final = final + 2
            somatres = somatres + final
            if contador == primeiro:
                somatres += ((2 * primeiro) - 1)
        contador = contador + 1
    print(f'O resultado do terceiro é {somatres}')
except ValueError:
    print('ERRO!!! Valor digitado inválido')