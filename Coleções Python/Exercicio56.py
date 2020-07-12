"""
56. Leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas. em seguida, escreva o número de
alunos cuja pior nota foi na prova 1, o número de alunos cuja pior nota foi na prova 2, e o número
de alunos cuja pior nota foi na prova 3. Em caso de empate das piores notas de um aluno, o critério
de desempate é arbitrário, mas o aluno deve ser contabilizado apenas uma vez.
"""
matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
piornotas = []


for i in range(0, 3):
    for j in range(0, 10):
        matriz[i][j] = float(input(f'Aluno {i+1} - Prova {j+1} Insira a sua nota:  '))

i = 0
index = 0
for i in range(0, 3):
    for index,j in range(0, 10):
        if matriz[i][j] < matriz[i][index]:
            index = j
        piornotas.append(index)

