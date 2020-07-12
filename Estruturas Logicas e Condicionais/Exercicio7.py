"""
7. Faça um programa que receba dois números e mostre o maior. se por acaso, os dois números
forem iguais, imprima a mensagem 'numeros iguais'.
"""
num1 = float(input('Insira o seu primero número:'))
num2 = float(input('Insira o seu segundo número:'))
if num1 > num2:
    print(f'O seu primeiro valor:{num1} é o maior que o segundo valor:{num2}')
elif num1 == num2:
    print('Números iguais')
else:
    print(f'O seu segundo valor:{num2} é o maior que o primeiro valor:{num1}')