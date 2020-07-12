"""
43. Leia uma matriz de 4 x 4, imprima a matriz e retome a localização (linha e a coluna) do maior valor
"""
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
maior = 0
posicao = 0

for i in range(0, 4):
    for c in range(0, 4):
        matriz[i][c] = float(input(f'Digite um valor para matriz [{[i]} {[c]}]:  '))
        if (i == 0) and (c == 0):
            maior = matriz[i][c]
        if matriz[i][c] > maior:
            maior = matriz[i][c]
            posicao = [i, c]

for i in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[i][c]}]', end=' ')
    print()

print(f'O maior valor: {maior}\nFica localizado na matriz [{posicao}]')