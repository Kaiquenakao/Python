"""
54. Leia uma matriz 5 x 10 que se refere respostas de 10 questões de múltiplica escolha, referentes
a 5 alunos. Leia também um vetor de 10 posições contendo o gabarito de respostas que podem er a, b, c
ou d. Seu programa deverá comparar as respostas de cada candidato com gabarito e emitir um vetor
denominando resultado, contendo a pontuação correspondente a cada aluno.
"""
matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
gabarito = ['a', 'b', 'c', 'd', 'a', 'a', 'c', 'a', 'd', 'b']
resultado = []

cont = 0
for i in range(0, 5):
    cont = 0
    for j in range(0, 10):
        matriz[i][j] = input(f'Aluno {i+1} - Questão {j+1} Digite a resposta:  ')
        if matriz[i][j] in gabarito[j]:
            print('acertou!!')
            cont = cont + 1
    resultado.append(cont)

for i in range(0, 5):
    for j in range(0, 10):
        print(matriz[i][j])

print(f'Gabarito: {gabarito}')

for i in range(0, 5):
    print(f'Aluno {i+1} - tirou {resultado[i]} de nota!!!')