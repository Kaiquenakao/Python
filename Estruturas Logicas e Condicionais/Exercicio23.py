"""
23. Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto e for
divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo exemplo:
1988, 1992, 1996.
"""
try:
    ano = int(input('Insira o ano para saber se ele é bissexto:  '))
    if ano % 400 == 0 or ano % 4 == 0 and not ano % 100 == 0:
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')
except ValueError:
    print('ERRO!!! o número digitado precisa ser inteiro')