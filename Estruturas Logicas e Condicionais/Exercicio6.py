"""
6. Escreva um programa que, dados dois números inteiros, mostre na tela o maior dele, assim
como a diferença existente entre ambos.
"""
num1 = int(input('Insira o seu primeiro valor:'))
num2 = int(input('Insira o seu segundo valor:'))
if num1 > num2:
    print(f'O seu primeiro valor:{num1} é o maior que o segundo valor:{num2}\nA diferença deles é {num1 - num2}.')
else:
    print(f'O seu segundo valor:{num2} é o maior que o primeiro valor:{num1}\nA diferença deles é {num2 - num1}.')