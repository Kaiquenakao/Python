"""
30. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspodente
em dólares
"""
real = float(input('Insira o valor do real:  '))
cotacao = float(input('Insira a cotação do dólar:  '))
compra = real / cotacao
print(f'O valor correspondente em dólar: {"%.3f" % compra}')