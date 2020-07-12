"""
38. Faça um programa que calcule o terno pitagórico a, b, c, para o qual a + b + c = 1000.
Um terno pitagórico é um conjunto de três números naturais, a, b, c para qual,
        a² + b² = c²
por exemplo,
        3² + 4² = 9 + 16 = 25 = 5²
"""
a = int(input('Insira um número natural para o a:  '))
b = int(input('Insira um número natural para o b:  '))
c = int(input('Insira um número para o c: '))

print(f'{a}² + {b}² = {pow(a, 2)} + {pow(b, 2)} = {(pow(a, 2) + pow(b, 2))}')
if (pow(a, 2) + pow(b, 2)) / c == c:
    print(f'{(pow(a, 2) + pow(b, 2)) / c}² é um aterno pitagórico')
else:
    print(f'Não é um aterno pitagórico {(pow(a, 2) + pow(b, 2)) / c}')
