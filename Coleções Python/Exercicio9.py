"""
9. Crie um programa lê 6 primeiros inteiros e pares, em seguida, mostre na tela os valores
lidos na ordem inversa
"""
global contador, i
i = 0
contador = 0
vetor = []
while(contador < 6):
    i = i + 1
    numeros = int(input(f'Posição{i}:Insira um valor par:'))
    if numeros % 2 == 0:
        vetor.append(numeros)
        contador = contador + 1
    else:
        break
print(vetor[::-1])


