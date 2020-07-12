"""
32. Leia um número inteiro e imprima a soma do sucessor de seu triplo com antecessor
do seu dobro.
"""
try:
    inteiro = int(input('Insira um número inteiro:  '))
    triplo = (inteiro + 1) * 3
    antecessor = (inteiro - 1) * 2
    soma = triplo + antecessor
    print(f'A soma do triplo do sucessor {triplo} mais o'
     f' dobro do antecessor {antecessor} é igual a {triplo + antecessor}')
except ValueError:
    print(f'Erro!! o seu número não é inteiro')
