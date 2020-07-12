"""
61. Faça um programa que calcule o maior número palíndromo feito a partir do produto de dois números
de 3 dígitos. Ex: O maior palíndromo feito a partir do produto de dois números digitados é
9009 = 91 * 99.
"""
palindromo = input('Insira um número de 3 dígitos: ')
palindromo2 = input('Insira um número de 3 dígitos:  ')
separador = int(palindromo)
separador2 = int(palindromo2)
print(f'O produto de dois números com 3 digitos é {palindromo+palindromo2} = {separador} * {separador2}  = '
      f'{separador * separador2}')