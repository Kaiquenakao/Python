"""
7. Escreva um programa que leia 10 números inteiros e os armazene em um vetor. imprima
o vetor, o maior elemento e a posição que ele se encontra.
"""
global contador
contador = 1
vetor = []
for i in range(1,10+1):
    numeros = int(input(f'Posição{i}:Insira o seu valor:'))
    vetor.append(numeros)
print(vetor)
x = max(vetor)
def posicao(x,contador,*args):
    for num in args:
        if num == x:
            return contador
        else:
            contador = contador + 1
print(f'A sua posição: {posicao(x,contador,*vetor)}')
