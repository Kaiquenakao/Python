"""
46. Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da mesma forma:
A[i][j] = 2i + 7j - 2 se i < j;
A[i][j] = 3i² - 1 se i = j
A[i][j] = 4i³ - 5j² + 1 se i > j
"""
A = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            A[i][j] = 2 * i + 7 * j - 2
        if i == j:
            A[i][j] = 3 * pow(i, 2) - 1
        if i > j:
            A[i][j] = (4 * pow(i, 3)) - (5 * pow(j, 2)) + 1

print('---------------RESULTADO FINAL-------------\n')

for i in range(0, 10):
    for j in range(0, 10):
        print(f'[{A[i][j]}]', end=' ')
    print()