"""
5. Faça um programa que peça ao usuário para digitar 10 valores e some-os.
"""
global soma
soma = 0
for num in range(1,10+1):
    numeros = float(input(f'Posição{num}:Digite um número:'))
    soma = soma + numeros
print(soma)