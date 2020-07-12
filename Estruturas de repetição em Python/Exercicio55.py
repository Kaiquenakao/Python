"""
55. Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros
números primos.
"""
contador = 1
lista = []
impar = 0

n = int(input('Insira "n" número primos:  '))

while True:
    contador = contador + 1
    if contador == 2 or contador == 3 or contador == 5 or contador == 7:
        lista.append(contador)
        impar += 1
    if not (contador % 2 == 0 or contador % 3 == 0 or contador % 5 == 0 or contador % 7 == 0):
        lista.append(contador)
        impar = impar + 1
    if impar == n:
        print(lista)
        break

print(f'A soma dos primeiros números {impar} ímpares: {sum(lista)}')

