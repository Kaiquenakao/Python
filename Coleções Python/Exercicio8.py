"""
8. Crie um programa que lê 6 valores inteiros, em seguida, mostre na tela os valores lidos
na ordem inversa
"""
vetor = []
for i in range(1,6+1):
    numeros = int(input(f'Posição{i}:Insira o seu valor:'))
    vetor.append(numeros)
print(vetor[::-1])