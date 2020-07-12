"""
56. Faça um programa que calcule a soma de todos os usuarios primos abaixos de dois milhões
"""
contador = 1
lista = []
impar = 0

while True:
    contador = contador + 1
    if contador == 2 or contador == 3 or contador == 5 or contador == 7:
        lista.append(contador)
        impar += 1
    if not (contador % 2 == 0 or contador % 3 == 0 or contador % 5 == 0 or contador % 7 == 0 or contador == 1):
        lista.append(contador)
        impar = impar + 1
    if impar == 2000000:
        break

print(f'a soma dos 2 milhões números primos: {sum(lista)}')

