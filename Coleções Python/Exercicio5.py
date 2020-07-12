""""
5. Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""
lista = []
global contador
contador = 0
for i in range(1,10+1):
    numeros = float(input(f'Posição{i}:Insira um número:'))
    lista.append(numeros)
    if numeros % 2 == 0:
        contador = contador + 1

print(f'Vetor: {lista}')
print(f'Pares: {[pares for pares in lista if pares % 2 == 0]}')
print(f'Valores pares:{contador}')