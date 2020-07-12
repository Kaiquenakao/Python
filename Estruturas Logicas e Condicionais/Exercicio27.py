"""
27. Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes
categorias:
---------------------------------------
|   Categoria    | idade              |
|   Infantil A   | 5 a 7              |
|   Infantil B   | 8 a 10             |
|   Juvenil A    | 11 a 13            |
|   Juvenil B    | 14 a 17            |
|   Sênior       | Maiores de 18 anos |
---------------------------------------
"""
try:
    idade = int(input('Insira a idade do nadador:  '))
    if (idade >= 5) and (idade <= 7):
        print('Categoria: Infantil A')
    if (idade >= 8) and (idade <= 10):
        print('Categoria: Infantil B')
    if (idade >= 11) and (idade <= 13):
        print('Categoria: Juvenil A')
    if (idade >= 14) and (idade <= 17):
        print('Categoria: Juvenil B')
    if idade >= 18:
        print('Categoria: Sênior')
except ValueError:
    print('ERRO!!! Só pode ser digitado números inteiros')