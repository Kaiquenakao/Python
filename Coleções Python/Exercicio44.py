"""
44. Leia uma matriz de 5 x 5. Leia também um valor X. o programa deverá fazer uma busca desse valor
na matriz e, no final, escrever a localização (linha e coluna) ou uma mensagem de 'não encontrado'
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
posicao = 0
contadorf = 0
contador = 0

x = float(input('Insira um valor do x:  '))
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = float(input(f'Matriz [{[i]} {[j]}] insira um valor:  '))
        if x == matriz[i][j]:
            posicao = [i, j]
            contador = 1

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]}]', end=' ')
    print()

if contador == 1:
    print(f'Valor encontrado {posicao}')
else:
    print(f'Valor não encontrado')